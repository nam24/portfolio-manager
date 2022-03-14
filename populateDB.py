import psycopg2
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

class PopulateDB:
    def populateMFTransactionsFromCSV():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing table
        cursor.execute(Queries.dropTableQ(DBConstants.mfTransactions))

        #create MF transactions table
        cursor.execute(Queries.createMFTransactionsTableQ)
        cursor.execute(Queries.importCSVQ(DBConstants.mfTransactions, "cas.csv"))

        #amc, scheme-name, isin, amfi, pan
        cursor.execute(Queries.getAllMFTransactionsQ)
        line = cursor.fetchall()
        print(line[0])

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)
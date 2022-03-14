import psycopg2
from helper import HelperFunctions
from queries import Queries

class PopulateDB:
    def populateMFTransactionsFromCSV():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
                
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # drop pre-existing table
        cursor.execute(Queries.dropTableQ)

        #create MF transactions table
        cursor.execute(Queries.createTableQ)
        cursor.execute(Queries.importCSVQ)

        #amc, scheme-name, isin, amfi, pan
        cursor.execute(Queries.getAllMFTransactionsQ)
        line = cursor.fetchall()
        print(line[0])

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)
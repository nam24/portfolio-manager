import this
import psycopg2

from queries import Queries

class HelperFunctions:
    def getListOfAllMFTransactions():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing table
        cursor.execute(Queries.getAllMFTransactionsQ)
        data = cursor.fetchall()

        HelperFunctions.closeDbConnection()
        return data

    def getDbConnectionObject(database, user):
        #establishing the connection
        # add roles and passwords
        conn = psycopg2.connect( database= database, user= user, host= '127.0.0.1', port= '5432') 
        return conn

    def closeDbConnection(connection):
        connection.close()
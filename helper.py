import psycopg2

class HelperFunctions:
    def getListOfAllMFTransactions():
        return 1
    
    def getDbConnectionObject(database, user):
        #establishing the connection
        # add roles and passwords
        conn = psycopg2.connect( database= database, user= user, host= '127.0.0.1', port= '5432') 
        return conn

    def closeDbConnection(connection):
        connection.close()
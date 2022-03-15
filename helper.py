import psycopg2
from dbConstants import DBConstants

from queries import Queries

class HelperFunctions:
    def getListOfAllMFTransactions():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing table
        cursor.execute(Queries.getAllFromTable(DBConstants.mfTransactions))
        data = cursor.fetchall()
        '''
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2])

        # creating list       
list = [] 
  
# appending instances to list 
list.append( geeks('Akash', 2) )
list.append( geeks('Deependra', 40) )

'''

        HelperFunctions.closeDbConnection()
        return data

    def getDbConnectionObject(database, user):
        #establishing the connection
        # add roles and passwords
        conn = psycopg2.connect( database= database, user= user, host= '127.0.0.1', port= '5432') 
        return conn

    def closeDbConnection(connection):
        connection.close()
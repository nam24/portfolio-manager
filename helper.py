from time import sleep
import psycopg2
from applescript import tell
from dbConstants import DBConstants
from objects import MFTransactions

from queries import Queries

class HelperFunctions:
    def getListOfAllMFTransactions():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        cursor.execute(Queries.getAllFromTable(DBConstants.mfTransactions))
        data = cursor.fetchall()
        print(data)

        mftransactions = []
        for tuple in data:
            print(tuple)
            mftransactions.append(MFTransactions(tuple))
            print("done \n")

        HelperFunctions.closeDbConnection(conn)
        return mftransactions

    def getDbConnectionObject(database, user):
        #establishing the connection
        # add roles and passwords
        startConnectionCmd = 'brew services start postgresql'
        tell.app('Terminal', 'do script "' + startConnectionCmd + '"' + 'in window 1') 
        sleep(5)
        conn = psycopg2.connect(database= database, user= user, host= '127.0.0.1', port= '5432') 
        return conn

    def closeDbConnection(connection):
        connection.close()
        stopConnectionCmd = 'brew services stop postgresql'
        tell.app('Terminal', 'do script "' + stopConnectionCmd + '"' + 'in window 1') 


from time import sleep
import psycopg2
from applescript import tell
from dbConstants import DBConstants
from objects import MFTransactions

from queries import Queries

class HelperFunctions:
    def getTotalAmountByTransactionType(mfTransactions, type):
        def filterByType(x):
            if(x.type == type):
                return x.amount
            return 0

        return sum(map(filterByType, mfTransactions))

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


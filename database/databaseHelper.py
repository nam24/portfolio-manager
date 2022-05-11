from time import sleep
import psycopg2
from applescript import tell

class DatabaseHelperFunctions:
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

# <https://sourabhbajaj.com/mac-setup/PostgreSQL/>
# <https://dataschool.com/learn-sql/how-to-start-a-postgresql-server-on-mac-os-x/>
import psycopg2
from queries import Queries

class PopulateDB:
    def populateMFTransactionsFromCSV():
        #establishing the connection
        conn = psycopg2.connect(
        database="finance", user='namrata', host='127.0.0.1', port= '5432'
        ) # add roles and passwords

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
        conn.close()
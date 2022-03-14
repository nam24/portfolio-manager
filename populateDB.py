from time import sleep
from createCSV import CreateCSV
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

class RefreshDb:
    def refreshDb(refreshFiles, refreshTables):
        # For MFs
        if(refreshFiles):
            CreateCSV.createCSVFromPDF()
            sleep(15)
        if(refreshTables):
            RefreshDb.refreshMFTablesFromCSVs()
        
    def refreshMFTablesFromCSVs():
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing tables
        cursor.execute(Queries.dropTableQ(DBConstants.mfTransactions))
        cursor.execute(Queries.dropTableQ(DBConstants.mfInfo))
        cursor.execute(Queries.dropTableQ(DBConstants.mfValues))

        #create MF tables
        cursor.execute(Queries.createMFTablesQ())

        cursor.execute(Queries.getAllFromTable(DBConstants.mfTransactions))
        line = cursor.fetchall()
        print("\n\n")
        print(line)

        cursor.execute(Queries.getAllFromTable(DBConstants.mfInfo))
        line = cursor.fetchall()
        print("\n\n")
        print(line)

        cursor.execute(Queries.getAllFromTable(DBConstants.mfValues))
        line = cursor.fetchall()
        print("\n\n")
        print(line)

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)
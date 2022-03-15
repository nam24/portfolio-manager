from time import sleep
from objects import MFTransactions
from createCSV import CreateCSV
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

class CalculateDb:
    def calculateDb(newCASFile=0, recalculateTables=1):
        # For MFs
        if(newCASFile):
            CreateCSV.createCSVFromPDF()
            sleep(15)

        db = CalculateDb.calculateMFTablesFromCSVs(recalculateTables)

        return db
        
    def calculateMFTablesFromCSVs(recalculateTables):
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing tables
        cursor.execute(Queries.dropTableQ(DBConstants.mfTransactions))
        cursor.execute(Queries.dropTableQ(DBConstants.mfInfo))
        cursor.execute(Queries.dropTableQ(DBConstants.mfValues))

        #create MF tables
        cursor.execute(Queries.createMFTablesQ())

        cursor.execute(Queries.getAllFromTable(DBConstants.mfTransactions))
        data = cursor.fetchall()
        print("\n\n")
        print(data)
        mftransactions = []
        for tuple in data:
            #print(tuple)
            mftransactions.append(MFTransactions(tuple))
            #print("done \n")

        # db.mfTransactions = mftransactions
        cursor.execute(Queries.getAllFromTable(DBConstants.mfInfo))
        line = cursor.fetchmany(5)
        print("\n\n")
        print(line)

        cursor.execute(Queries.getAllFromTable(DBConstants.mfValues))
        line = cursor.fetchmany(5)
        print("\n\n")
        print(line)

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)

        return {}
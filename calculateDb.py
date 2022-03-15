from time import sleep
from objects import MFTransactions, MFInfo, MFValues, Db
from createCSV import CreateCSV
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

class CalculateDb:
    def calculateDb(newCASFile=0):
        # For MFs
        if(newCASFile):
            CreateCSV.createCSVFromPDF()
            sleep(15)

        db = CalculateDb.calculateMFTablesFromCSVs()
        return db
        
    def calculateMFTablesFromCSVs():
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
        print(data[0])
        mftransactions = []
        for tuple in data:
            print(tuple)
            mftransactions.append(MFTransactions(tuple))
            print("done \n")

        # db.mfTransactions = mftransactions
        cursor.execute(Queries.getAllFromTable(DBConstants.mfInfo))
        data = cursor.fetchall()
        print("\n\n")
        print(data[0])
        mfInfo = []
        for tuple in data:
            #print(tuple)
            mfInfo.append(MFInfo(tuple))
            #print("done \n")

        cursor.execute(Queries.getAllFromTable(DBConstants.mfValues))
        data = cursor.fetchall()
        print("\n\n")
        print(data[0])
        mfValues = []
        for tuple in data:
            #print(tuple)
            mfValues.append(MFValues(tuple))
            #print("done \n")

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)

        return Db(mftransactions, mfInfo, mfValues)
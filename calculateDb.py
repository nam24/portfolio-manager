from time import sleep
from objects import MFTransactions, MFInfo, MFValues, Db
from createCSV import CreateCSV
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

class CalculateDb:
    def calculateDb(newCASFile=0):
        # If we want to create new csv files from pdf
        if(newCASFile):
            CreateCSV.createCSVFromPDF()
            sleep(15)

        # Populates the postgresql database from cas.csv
        # Currently this needs to be done everytime, need to find
        # a way to retain the tables
        return CalculateDb.calculateMFTablesFromCSVs()
        
    def calculateMFTablesFromCSVs():
        # DB name = 'finance', user = 'namrata'
        conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing tables
        # can make this optional when we find a way to retain tables
        cursor.execute(Queries.dropTableQ(DBConstants.mfTransactions))
        cursor.execute(Queries.dropTableQ(DBConstants.mfInfo))
        cursor.execute(Queries.dropTableQ(DBConstants.mfValues))

        #create MF tables
        cursor.execute(Queries.createMFTablesQ())

        cursor.execute(Queries.getAllFromTable(DBConstants.mfTransactions))
        data = cursor.fetchall()
        print("\n\n")
        mfTransactions = []
        for tuple in data:
            mfTransactions.append(MFTransactions(tuple))

        cursor.execute(Queries.getAllFromTable(DBConstants.mfInfo))
        data = cursor.fetchall()
        print("\n\n")
        mfInfo = []
        for tuple in data:
            mfInfo.append(MFInfo(tuple))

        cursor.execute(Queries.getAllFromTable(DBConstants.mfValues))
        data = cursor.fetchall()
        print("\n\n")
        mfValues = []
        for tuple in data:
            mfValues.append(MFValues(tuple))

        #Closing the connection
        HelperFunctions.closeDbConnection(conn)

        return Db(mfTransactions, mfInfo, mfValues)
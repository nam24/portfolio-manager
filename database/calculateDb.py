from time import sleep
from database.databaseHelper import DatabaseHelperFunctions
from objects import MFTransactions, MFInfo, MFValues, MFData
from database.createCSV import CreateCSV
from constants import Constants
from database.queries import Queries

class CalculateDb:
    def calculateDb(newCASFile=0, fileName='cas.pdf'):
        # If we want to create new csv files from pdf
        if(newCASFile):
            CreateCSV.createCSVFromPDF(fileName)
            sleep(15)

        # Populates the postgresql database from cas.csv
        # Currently this needs to be done everytime, need to find
        # a way to retain the tables
        return CalculateDb.calculateMFTablesFromCSVs()
        
    def calculateMFTablesFromCSVs():
        # DB name = 'finance', user = 'namrata'
        conn = DatabaseHelperFunctions.getDbConnectionObject('finance', 'namrata')
        cursor = conn.cursor()

        # drop pre-existing tables
        # can make this optional when we find a way to retain tables
        cursor.execute(Queries.dropTableQ(Constants.mfTransactions))
        cursor.execute(Queries.dropTableQ(Constants.mfInfo))
        cursor.execute(Queries.dropTableQ(Constants.mfValues))

        # Create MF tables:
        # mfTransactions 
        # mfInfo 
        # mfValues 
        cursor.execute(Queries.createMFTablesQ())

        # Get all data from postgres tables and store in Db object which is returned
        # This is a useless step at this point because the simpler way will be to extract
        # this data directly from csv (no need to create postgres db).
        # In any case, it doesn't make sense to have this functionality here. 
        cursor.execute(Queries.getAllFromTable(Constants.mfTransactions))
        data = cursor.fetchall()
        print("\n\n")
        mfTransactions = []
        for tuple in data:
            mfTransactions.append(MFTransactions(tuple))

        cursor.execute(Queries.getAllDisctinctFromTable(Constants.mfInfo))
        data = cursor.fetchall()
        print("\n\n")
        mfInfo = []
        for tuple in data:
            mfInfo.append(MFInfo(tuple))

        cursor.execute(Queries.getAllFromTable(Constants.mfValues))
        data = cursor.fetchall()
        print("\n\n")
        mfValues = []
        for tuple in data:
            mfValues.append(MFValues(tuple))

        return MFData(mfTransactions, mfInfo, mfValues)
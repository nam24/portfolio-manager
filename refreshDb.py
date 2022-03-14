from time import sleep
from createCSV import CreateCSV
from populateDB import PopulateDB

class RefreshDb:
    def refreshMFTransactions():
        CreateCSV.createCSVFromPDF()
        sleep(15)
        PopulateDB.populateMFTransactionsFromCSV()
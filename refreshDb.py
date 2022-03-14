from time import sleep
from createCSV import CreateCSV
from populateDB import PopulateDB

class RefreshDb:
    def refreshMFTransactions():
        CreateCSV.createCSVFromPDF()
        sleep(20)
        PopulateDB.populateMFTransactionsFromCSV()

# get total amount invested
# get total amount invested by scheme
# get total amount invested by AMC
# get curve of amt invested vs month
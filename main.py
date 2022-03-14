from time import sleep
from createCSV import CreateCSV
from populateDB import PopulateDB

CreateCSV.createCSVFromPDF()
sleep(5)
PopulateDB.populateDBFromCSV()

# get total amount invested
# get total amount invested by scheme
# get total amount invested by AMC
# get curve of amt invested vs month
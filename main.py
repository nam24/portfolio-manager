from time import sleep
from createCSV import CreateCSV
from populateDB import PopulateDB

CreateCSV.createCSVFromPDF()
sleep(5)
PopulateDB.populateDBFromCSV()
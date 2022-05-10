import sys
from database.calculateDb import CalculateDb
from reports.reports import Reports

newCasFile = 1 if(len(sys.argv)>1) else 0

# MFData class instance:
mfData = CalculateDb.calculateDb(newCasFile)

# Create report
Reports.calculateReports(mfData)
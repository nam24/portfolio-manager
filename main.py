from fileinput import filename
import sys
from database.calculateDb import CalculateDb
from reports.reports import Reports

newCasFile = sys.argv[1] if(len(sys.argv)>1) else 0
fileName = sys.argv[2] if(len(sys.argv)>2) else 'cas.pdf'

# MFData class instance:
mfData = CalculateDb.calculateDb(newCasFile, fileName)

# Create report
Reports.calculateReports(mfData)
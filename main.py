from database.calculateDb import CalculateDb
from reportHelper import ReportHelperFunctions
from dbConstants import Constants
from reports import Reports

# MFData class instance:
mfData = CalculateDb.calculateDb(0)

# Create report
Reports.calculateReports(mfData)
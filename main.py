from database.calculateDb import CalculateDb
from reports.reports import Reports

# MFData class instance:
mfData = CalculateDb.calculateDb(0)

# Create report
Reports.calculateReports(mfData)
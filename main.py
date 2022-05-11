from fileinput import filename
import sys
from constants import Constants
from database.calculateDb import CalculateDb
from reports.reports import Reports

args = dict()
argsKeys = ['scriptName', 'newCasFile', 'fileName', 'filePassword', 'fileLocation']

args['newCasFile'] = False
args['fileName'] = Constants.defaultFileName
args['filePassword'] = Constants.defaultFilePassword
args['fileLocation'] = Constants.defaultFileLocation

for idx, arg in enumerate(sys.argv):
    args[argsKeys[idx]] = arg
for arg in args:
    print(arg, end = ": ")
    print(args[arg])

# MFData class instance:
mfData = CalculateDb.calculateDb(args[argsKeys[1]], args[argsKeys[2]], args[argsKeys[3]], args[argsKeys[4]])

# Create report
Reports.calculateReports(mfData)
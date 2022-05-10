from applescript import tell
from dbConstants import DBConstants

# This script creates CSV files using a cli tool- 
# (1) detailed with all transactions (cas.csv) and 
# (2) summary of all portfolios and schemes (cas-summary.csv)

# The source pdf (cas.pdf) with password 'abcdefgh12' should be saved in the 'Files' folder
# Processed files will be saved in the same location

class CreateCSV:
    def createCSVFromPDF():
        switchDirCmd = 'cd ' + DBConstants.filesLocation
        exportFullCSVCmd = 'casparser -o cas.csv -p abcdefgh12 cas.pdf'
        exportSummaryCSVCmd = 'casparser -o cas-summary.csv -p abcdefgh12 -s -a cas.pdf'
        tell.app('Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
        tell.app('Terminal', 'do script "' + exportFullCSVCmd + '"' + 'in window 1') 
        tell.app('Terminal', 'do script "' + exportSummaryCSVCmd + '"' + 'in window 1')
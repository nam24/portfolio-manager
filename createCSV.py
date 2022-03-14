from applescript import tell
from dbConstants import DBConstants

class CreateCSV:
    def createCSVFromPDF():
        switchDirCmd = 'cd ' + DBConstants.filesLocation
        exportFullCSVCmd = 'casparser -o cas.csv -p abcdefgh12 cas.pdf'
        exportSummaryCSVCmd = 'casparser -o cas-summary.csv -p abcdefgh12 -s -a cas.pdf'
        tell.app( 'Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
        tell.app( 'Terminal', 'do script "' + exportFullCSVCmd + '"' + 'in window 1') 
        tell.app( 'Terminal', 'do script "' + exportSummaryCSVCmd + '"' + 'in window 1')
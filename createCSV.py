from applescript import tell

class CreateCSV:
    def createCSVFromPDF():
        switchDirCmd = 'cd /Users/namrata/Documents/PM/Files'
        exportFullCSVCmd = 'casparser -o cas.csv -p abcdefgh12 cas.pdf'
        exportSummaryCSVCmd = 'casparser -o cas-summary.csv -p abcdefgh12 -s -a cas.pdf'
        tell.app( 'Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
        tell.app( 'Terminal', 'do script "' + exportFullCSVCmd + '"' + 'in window 1') 
        tell.app( 'Terminal', 'do script "' + exportSummaryCSVCmd + '"' + 'in window 1')
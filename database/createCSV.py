from applescript import tell
from constants import Constants

# This script creates CSV files using a cli tool- 
# (1) detailed with all transactions (cas.csv) and 
# (2) summary of all portfolios and schemes (cas-summary.csv)

# The source pdf (cas.pdf) with password 'abcdefgh12' should be saved in the 'Files' folder
# Processed files will be saved in the same location

class CreateCSV:
    def createCSVFromPDF():
        switchDirCmd = 'cd ' + Constants.filesLocation
        exportFullCSVCmd = 'casparser -o cas.csv -p abcdefgh12 cas.pdf'
        exportSummaryCSVCmd = 'casparser -o cas-summary.csv -p abcdefgh12 -s -a cas.pdf'
        tell.app('Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
        tell.app('Terminal', 'do script "' + exportFullCSVCmd + '"' + 'in window 1') 
        tell.app('Terminal', 'do script "' + exportSummaryCSVCmd + '"' + 'in window 1')

# CLI-based tool: https://github.com/janiniraj/casparser

# Usage: casparser [-o output_file.json|output_file.csv] [-p password] [-s] [-a] CAS_PDF_FILE

#   -o, --output FILE               Output file path. Saves the parsed data as json or csv
#                                   depending on the file extension. For other extensions, the
#                                   summary output is saved. [See note below]

#   -s, --summary                   Print Summary of transactions parsed.
#   -p PASSWORD                     CAS password
#   -a, --include-all               Include schemes with zero valuation in the
#                                   summary output
#   --force-pdfminer                Force PDFMiner parser even if MuPDF is
#                                   detected

#   --version                       Show the version and exit.
#   -h, --help                      Show this message and exit.
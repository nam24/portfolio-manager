from applescript import tell

switchDirCmd = 'cd /Users/namrata/Documents/Python'
exportCSVCmd = 'casparser -o output_file.csv -p abcdefgh12 -s -a cas.pdf'
tell.app( 'Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
tell.app( 'Terminal', 'do script "' + exportCSVCmd + '"' + 'in window 1') 
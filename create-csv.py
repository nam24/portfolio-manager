from applescript import tell

switchDirCmd = 'cd /Users/namrata/Documents/PM'
exportCSVCmd = 'casparser -o cas.csv -p abcdefgh12 -s -a cas.pdf'
tell.app( 'Terminal', 'do script "' + switchDirCmd + '"' + 'in window 1') 
tell.app( 'Terminal', 'do script "' + exportCSVCmd + '"' + 'in window 1') 
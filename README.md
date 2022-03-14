# portfolio-manager
Manage investments portfolio

CLI-based tool: https://github.com/janiniraj/casparser
This also has a library, but doesn't work well
casparser.json is created using this

Usage: casparser [-o output_file.json|output_file.csv] [-p password] [-s] [-a] CAS_PDF_FILE

  -o, --output FILE               Output file path. Saves the parsed data as json or csv
                                  depending on the file extension. For other extensions, the
                                  summary output is saved. [See note below]

  -s, --summary                   Print Summary of transactions parsed.
  -p PASSWORD                     CAS password
  -a, --include-all               Include schemes with zero valuation in the
                                  summary output
  --sort                          Sort transactions by date
  --force-pdfminer                Force PDFMiner parser even if MuPDF is
                                  detected

  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.




postgresql:
https://sourabhbajaj.com/mac-setup/PostgreSQL/
https://dataschool.com/learn-sql/how-to-start-a-postgresql-server-on-mac-os-x/

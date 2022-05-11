# Portfolio Management Utility

Get top level analytics for mutual fund portfolios.
This script utilizes cas pdf to:
    - get aggregated numbers and summaries- to help manage spread out mutual fund invesmtents.
    - get a list of long-term capital gains eligible purchases (ELSS and non-ELSS)

More analytics to be added based on requirement.

The source pdf (default: cas.pdf) with password filePassword (default: 'abcdefgh12') should be saved in fileLocation

python3 main.py filesLocation newCasFile fileName filePassword
python3 main.py 1 filename  ...... if new cas file

Args:

1. newCASFile: boolean
2. fileName: string
3. filePassword: string (wip)
4. filepath: string (wip)

# Portfolio Management Utility

Get top level analytics for mutual fund portfolios.
This script utilizes cas pdf to:
    - get aggregated numbers and summaries- to help manage spread out mutual fund invesmtents.
    - get a list of long-term capital gains eligible purchases (ELSS and non-ELSS)
    - export these numbers to a excel

More analytics to be added based on requirement.

When running for the first time (or with a new cas pdf), all arguments must be given as input:
```python3 main.py filesLocation newCasFile fileName filePassword```

Once csv files have been created, they may be used to generate analysis without a cas pdf.
python3 main.py filesLocation

Args:

1. fileLocation : string  -  location of the directory where csv/ pdf file is stored
2. newCASFile   : boolean -  true if new cas pdf is to be used (1/0 or true/false)  :  (default: false) 
3. fileName     : string  -  name of the cas pdf including extension                :  (default: cas.pdf)
4. filePassword : string  -  password of the cas pdf                                :  (default: abcdefgh12)

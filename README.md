# Portfolio Management Utility

## Get top level analytics for mutual fund portfolios

### This script utilizes cas pdf to

1. get aggregated numbers and summaries- to help manage spread out mutual fund invesmtents.
2. get a list of long-term capital gains eligible purchases (ELSS and non-ELSS)
3. export these numbers to a excel

More analytics to be added based on requirement.

### Running the script

When running for the first time (or with a new cas pdf), all arguments must be given as input:

```python3 main.py filesLocation newCasFile fileName filePassword```

Once csv files have been created, they may be used to run analysis without a cas pdf:

```python3 main.py filesLocation```

#### Args

```sh
fileLocation : string  -  location of the directory where csv/ pdf file is stored
newCASFile   : boolean -  1 when new cas pdf is to be used (1/0 or true/false)  :  (default: false) 
fileName     : string  -  name of the cas pdf including extension                :  (default: cas.pdf)
filePassword : string  -  password of the cas pdf                                :  (default: abcdefgh12)
```

#### Generating a cas pdf

CAS is a "Consolidated Account Statement" issued by CAMS/KFintech. It contains a list of all your investments linked to your email ID & PAN.

1. Go to <https://www.camsonline.com/Investors/Statements/Consolidated-Account-Statement>
2. Select statement type - Detailed
3. Input all other fields according to requirement and submit. You will get the pdf on your email within 1 day.

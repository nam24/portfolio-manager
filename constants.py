class Constants:
    filesLocation = '/Users/namrata/Documents/PM/Files/'

    # Postgresql tables
    mfTransactions = 'mftransactions'
    mfInfo = 'mfinfo'    
    mfValues = 'mfvalues'

    # Transaction types
    PURCHASE_SIP = 'PURCHASE_SIP'
    PURCHASE = 'PURCHASE'
    REVERSAL = 'REVERSAL' # Kotak's refund
    REDEMPTION = 'REDEMPTION'
    STAMP_DUTY_TAX = 'STAMP_DUTY_TAX'   
    MISC = 'MISC' # Transaction charges for Axis Midcap Regular and Mirae Assets Refund (which has been 'cleaned')
    STT_TAX = 'STT_TAX' # Redemption of Axis Midcap Regular

    transactionTypes = [MISC, PURCHASE_SIP, PURCHASE, REDEMPTION, REVERSAL, STAMP_DUTY_TAX, STT_TAX]

    ELSS_FUNDS = [
        'Quant Tax Plan - Direct Plan',
        'Canara Robeco Equity Tax Saver Fund - Direct Growth',
        'Mirae Asset Tax Saver Fund - Direct Growth',
        'Axis Long Term Equity Fund - Direct Growth'
    ]
    FundsByMC = {
        'LargeCap':[],
        'MidCap':[],
        'SmallCap':[],
        'LargeMidCap':[],
        'MultiCap':[],
        'FlexiCap':[],
        'Focused':[],
        'ELSS': ELSS_FUNDS
    }

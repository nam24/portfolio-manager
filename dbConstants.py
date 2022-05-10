class DBConstants:
    filesLocation = '/Users/namrata/Documents/PM/Files/'

    # Postgresql tables
    mfTransactions = 'mftransactions'
    mfInfo = 'mfinfo'    
    mfValues = 'mfvalues'

    # Transaction types
    PURCHASE_SIP = 'PURCHASE_SIP'
    PURCHASE = 'PURCHASE'
    STAMP_DUTY_TAX = 'STAMP_DUTY_TAX'
    REVERSAL = 'REVERSAL' # Kotak's refund
    MISC = 'MISC' # Transaction charges for Axis Midcap Regular and Mirae Assets Refund
    REDEMPTION = 'REDEMPTION'
    STT_TAX = 'STT_TAX' # Redemption of Axis Midcap Regular

    transactionTypes = [MISC, PURCHASE_SIP, PURCHASE, REDEMPTION, REVERSAL, STAMP_DUTY_TAX, STT_TAX]
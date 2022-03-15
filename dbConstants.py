class DBConstants:
    filesLocation = '/Users/namrata/Documents/PM/Files/'

    mfTransactions = 'mftransactions'
    mfInfo = 'mfinfo'    
    mfValues = 'mfvalues'

    # Transaction types
    PURCHASE_SIP = 'PURCHASE_SIP'
    PURCHASE = 'PURCHASE'
    STAMP_DUTY_TAX = 'STAMP_DUTY_TAX'
    REVERSAL = 'REVERSAL'
    MISC = 'MISC'
    REDEMPTION = 'REDEMPTION'
    STT_TAX = 'STT_TAX'

    transactionTypes = [MISC, PURCHASE_SIP, PURCHASE, REDEMPTION, REVERSAL, STAMP_DUTY_TAX, STT_TAX]
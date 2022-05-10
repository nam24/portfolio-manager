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
    
    LARGECAP_FUNDS = [
        'Axis Bluechip Fund - Direct Growth',
    ]
    MIDCAP_FUNDS = [
        'Axis Mid Cap Fund - Direct Growth',
        'PGIM India Midcap Opportunities Fund - Direct Plan - Growth',
        'Kotak Emerging Equity Fund- Direct Plan - Growth',
    ]
    SMALLCAP_FUNDS = [
        'Axis Small Cap Fund Direct Growth',
        'Kotak Small Cap Fund - Direct Plan - Growth (Erstwhile Kotak Mid-Cap)',
    ]
    LARGEMIDCAP_FUNDS = [
        'Axis Growth Opportunities Fund Direct Growth',
    ]
    MULTICAP_FUNDS = [

    ]
    FLEXICAP_FUNDS = [

    ]
    FOCUSED_FUNDS = [
        'Axis Focused 25 Fund - Direct Plan - GROWTH',
    ]
    ELSS_FUNDS = [
        'Quant Tax Plan - Direct Plan',
        'Canara Robeco Equity Tax Saver Fund - Direct Growth',
        'Mirae Asset Tax Saver Fund - Direct Growth',
        'Axis Long Term Equity Fund - Direct Growth'
    ]

    FundsByMC = {
        'Large Cap': LARGECAP_FUNDS,
        'Mid Cap': MIDCAP_FUNDS,
        'Small Cap': SMALLCAP_FUNDS,
        'Large-Mid Cap': LARGEMIDCAP_FUNDS,
        'Multi Cap': MULTICAP_FUNDS,
        'Flexi Cap': FLEXICAP_FUNDS,
        'Focused': FOCUSED_FUNDS,
        'ELSS': ELSS_FUNDS
    }

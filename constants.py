class Constants:
    defaultFileName = 'cas.pdf'
    defaultFilePassword = 'abcdefgh12'
    defaultFileLocation = '/Users/namrata/Documents/PM/Files/'

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
        'Canara Robeco Blue Chip Equity Fund - Direct Growth',
        'Mirae Asset Large Cap Fund - Direct Plan - Growth',
    ]
    MIDCAP_FUNDS = [
        'Axis Mid Cap Fund - Direct Growth',
        'PGIM India Midcap Opportunities Fund - Direct Plan - Growth',
        'Kotak Emerging Equity Fund- Direct Plan - Growth',
        'Mirae Asset Midcap Fund Direct Plan - Growth',
        'Quant Mid Cap Fund - Growth',
    ]
    SMALLCAP_FUNDS = [
        'Axis Small Cap Fund Direct Growth',
        'Kotak Small Cap Fund - Direct Plan - Growth (Erstwhile Kotak Mid-Cap)',
        'Quant Small Cap Fund - Direct Plan Growth',
        'Canara Robeco Small Cap Fund - Direct Growth',
    ]
    LARGEMIDCAP_FUNDS = [
        'Axis Growth Opportunities Fund Direct Growth',
        'Canara Robeco Emerging Equities - Direct Growth',
        'Mirae Asset Emerging Bluechip Fund - Direct Plan - Growth',
    ]
    MULTICAP_FUNDS = [
        'Quant Active Fund - Growth',
    ]
    FLEXICAP_FUNDS = [
        'PGIM India Flexi Cap Fund - Direct Plan - Growth',
    ]
    FOCUSED_FUNDS = [
        'Axis Focused 25 Fund - Direct Plan - GROWTH',
        'Quant Infrastructure Fund - Direct Plan Growth',
        'Mirae Asset Focused Fund - Direct Plan - Growth',
        'Mirae Asset Healthcare Fund - Direct Plan - Growth',
    ]
    ELSS_FUNDS = [
        'Quant Tax Plan - Direct Plan',
        'Canara Robeco Equity Tax Saver Fund - Direct Growth',
        'Mirae Asset Tax Saver Fund - Direct Growth',
        'Axis Long Term Equity Fund - Direct Growth'
    ]

    FundsByCategory = {
        'Large Cap': LARGECAP_FUNDS,
        'Mid Cap': MIDCAP_FUNDS,
        'Small Cap': SMALLCAP_FUNDS,
        'Large-Mid Cap': LARGEMIDCAP_FUNDS,
        'Multi Cap': MULTICAP_FUNDS,
        'Flexi Cap': FLEXICAP_FUNDS,
        'Focused': FOCUSED_FUNDS,
        'ELSS': ELSS_FUNDS
    }

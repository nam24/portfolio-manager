from datetime import datetime
from constants import Constants
from reports.reportHelper import ReportHelperFunctions
from dateutil.relativedelta import relativedelta

class Reports:
    def calculateReports(mfData):
        # 1. Clean up the data
        # 2. Get numbers and print on console/ file
        mfData = ReportHelperFunctions.cleanUpDbObject(mfData)
        mfTransactions = mfData.mfTransactions
        # adjusting for redemptions. This contains all stamp duties and misc, though
        adjTransactions = ReportHelperFunctions.getRedemptionAdjustedTransactions(mfTransactions)
        purchaseTransactions = {x for x in adjTransactions if x.type in [Constants.PURCHASE, Constants.PURCHASE_SIP, Constants.REVERSAL]}

        print('Stamp Duty and other fees have not been included in the below numbers (unless specified).\n')        
        # Get top level fund nav summary
        Reports.calculateFundsNAVSummary(purchaseTransactions)
        # get market cap summary
        Reports.calculateMCNAVSummary(purchaseTransactions)
        # get transactions summary
        Reports.calculateTransactionsSummary(adjTransactions)
        # get LTCG: Long Term Capital Gain eligible transactions
        Reports.calculateLTCGeligibleTransactions(purchaseTransactions)

        
    def calculateFundsNAVSummary(purchaseTransactions):
        def fmt(x):
            return 'Rs. {:,.2f}'.format(x)
        totalAmountInvested = sum(map(lambda x: x.amount, purchaseTransactions))
        print('Total amount invested: ', round(totalAmountInvested, 2))
        allAMCs = set(list(map(lambda x: x.amc, purchaseTransactions)))
        allFunds = set(list(map(lambda x: x.scheme, purchaseTransactions)))
        allFolios = set(list(map(lambda x: x.folio, purchaseTransactions)))
        print('Total number of fund houses invested in: ', len(allAMCs))
        print('Total number of funds invested in: ', len(allFunds))
        print('Total number of folios invested in: ', len(allFolios))
        
        for amc in allAMCs:
            print()
            amctr = {z for z in purchaseTransactions if z.amc==amc}
            amt = sum(map(lambda z: z.amount, amctr))  
            print(f'  - {amc}: {fmt(amt)}')

            funds = set(list(map(lambda z: z.scheme, amctr)))
            for y in funds:
                fundtr = {z for z in amctr if z.scheme == y}
                amt = sum(map(lambda z: z.amount, fundtr))  
                print(f'    * {y}: {fmt(amt)}')
        print()
    
    def calculateMCNAVSummary(purchaseTransactions):
        def fmt(x):
            return 'Rs. {:,.2f}'.format(x)
        def fmt2(x):
            return '{:>15}'.format(x)
        print('Market Cap category distribution:')
        mcCategories = Constants.FundsByCategory.keys()
        totalAmt = sum(map(lambda x:x.amount, purchaseTransactions))

        for category in mcCategories:
            ctr = {x for x in purchaseTransactions if x.scheme in Constants.FundsByCategory[category]}
            amt = sum(map(lambda z: z.amount, ctr))  
            print(f'{fmt2(category)}: {fmt(amt)} ({round(amt*100/totalAmt, 2)}%)')
        print()

    def calculateTransactionsSummary(adjTransactions):
        def fmt(x):
            return 'Rs. {:,.2f}'.format(x)
        print('Adjusting for redemptions,')
        totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE_SIP])
        totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE])
        total = totalSIP + totalLumpSum
        totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(
                            adjTransactions, 
                            [Constants.STAMP_DUTY_TAX, Constants.MISC, Constants.STT_TAX]
                        )
        print(f'Total amount invested through SIPs: {fmt(totalSIP)} ({round(totalSIP*100/total,2)}%)')
        print(f'Total amount invested through lumpsum: {fmt(totalLumpSum)} ({round(totalLumpSum*100/total,2)}%)')
        print(f'Total others (stamp duty, transaction charges, redemption STT_Tax): {fmt(totalStampDuty)}')
        print()

    def calculateLTCGeligibleTransactions(purchaseTransactions):
        # LTCG: Long Term Capital Gain
        limit = datetime.date(datetime.now() - relativedelta(years=1, days=2))
        ltcgEligible = list({x for x in purchaseTransactions if 
                x.transactionDate<limit and x.scheme not in Constants.ELSS_FUNDS
                })
        ltcgEligible.sort(key=lambda x:x.transactionDate)

        print('Long Term Capital Gain Eligible Transactions (non-ELSS):')
        for k in ltcgEligible:
            print(f'{k.transactionDate} : {k.scheme} ({k.folio}) : {k.amount} : {k.units}')
        print()

        limitELSS = datetime.date(datetime.now() - relativedelta(years=3, days=2))
        tcgEligibleELSS = list({x for x in purchaseTransactions if 
                x.transactionDate<limitELSS and x.scheme in Constants.ELSS_FUNDS
                })
        tcgEligibleELSS.sort(key=lambda x:x.transactionDate)

        print('Long Term Capital Gain Eligible Transactions (ELSS):')
        for k in tcgEligibleELSS:
            print(f'{k.transactionDate} : {k.scheme} ({k.folio}) : {k.amount} : {k.units}')
        print()

        # Priority
                # print this data in excel
                # descending order preferrably - using grouping
                
                # adding sanity checks
                # testing
                # adding checks that csv is correct
        
        # Maybe
                # try and get number of SIPs and their dates and amounts by code
                # SIP chart - x axis shows dates in a month and y shows amount (find way to show which market cap)
                # show graphs in report??
                # get curve of amt invested vs month
                # get a txt report
                # no. of folios by fund
                # print all 3 tables in excel
                # adding args to main.py
                # treatment of reversals in LTCG calculation-- 
                #           not needed I think because -ve sign and some simple eyeballing
                # expense ratios
                # capital gains

        # Done
                # get total amount invested
                # Lumpsum vs SIP
                # top level summary- no. of amc, funds, folios
                # get total amount invested by AMC
                # get total amount invested by scheme
                # get % distribution in LC/MC/SC/L&MC...
                # add filename arg
                # proper documentation so that no time gone next time
                # fetch all long term capital gains eligible purchase transactions
                # currency formatting

                # how to treat redemptions?
                # compare units in folio and scheme subtract from 1st?---> complex
                # sum all except redemption. Rest of the claculation will require manual input
                # have another function for redeemed funds
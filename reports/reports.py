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
        
        # get transactions summary
        Reports.calculateTransactionsSummary(adjTransactions)
        # Get top level fund nav summary
        Reports.calculateFundsNAVSummary(purchaseTransactions)
        # get market cap summary
        Reports.calculateMCNAVSummary(purchaseTransactions)
        # get LTCG: Long Term Capital Gain eligible transactions
        Reports.calculateLTCGeligibleTransactions(purchaseTransactions)

    def calculateFundsNAVSummary(purchaseTransactions):
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
            print(f'  - {amc}: {Reports.fmt(amt)}')

            funds = set(list(map(lambda z: z.scheme, amctr)))
            for y in funds:
                fundtr = {z for z in amctr if z.scheme == y}
                amt = sum(map(lambda z: z.amount, fundtr))  
                print(f'    * {y}: {Reports.fmt(amt)}')
        print()
    
    def calculateMCNAVSummary(purchaseTransactions):
        def fmt(x):
            return 'Rs. {:,.2f}'.format(x)
        def fmt2(x):
            return '{:>15}'.format(x)
        print('Market Cap category distribution:')
        mcCategories = Constants.FundsByCategory.keys()
        totalAmt = sum(map(lambda x:x.amount, purchaseTransactions))
        d = dict()
        for category in mcCategories:
            ctr = {x for x in purchaseTransactions if x.scheme in Constants.FundsByCategory[category]}
            amt = sum(map(lambda z: z.amount, ctr))  
            d[category] = amt 
            print(f'{fmt2(category)}: {fmt(amt)} ({round(amt*100/totalAmt, 2)}%)')
        print()

    def calculateTransactionsSummary(adjTransactions):
        purchaseTransactions = {x for x in adjTransactions if x.type in [Constants.PURCHASE, Constants.PURCHASE_SIP, Constants.REVERSAL]}
        totalAmountInvested = sum(map(lambda x: x.amount, purchaseTransactions))
        totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE_SIP])
        totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE])
        total = totalSIP + totalLumpSum
        totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(
                            adjTransactions, 
                            [Constants.STAMP_DUTY_TAX, Constants.MISC, Constants.STT_TAX]
                        )
        print('Adjusting for redemptions,')
        print('Total amount invested: ', Reports.fmt(totalAmountInvested))
        print(f'Total amount invested through SIPs: {Reports.fmt(totalSIP)} ({round(totalSIP*100/total,2)}%)')
        print(f'Total amount invested through lumpsum: {Reports.fmt(totalLumpSum)} ({round(totalLumpSum*100/total,2)}%)')
        print(f'Total others (stamp duty, transaction charges, redemption STT_Tax): {Reports.fmt(totalStampDuty)}')
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

    def fmt(x):
        return 'Rs. {:,.2f}'.format(x)
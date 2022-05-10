from constants import Constants
from reports.reportHelper import ReportHelperFunctions

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

        
    def calculateFundsNAVSummary(purchaseTransactions):
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
            print(f'  - {amc}: {round(amt,2)}')

            funds = set(list(map(lambda z: z.scheme, amctr)))
            for y in funds:
                fundtr = {z for z in amctr if z.scheme == y}
                amt = sum(map(lambda z: z.amount, fundtr))  
                print(f'    * {y}: {round(amt,2)}')
        print()
    
    def calculateMCNAVSummary(purchaseTransactions):
        print('Market Cap category distribution:')
        mcCategories = Constants.FundsByCategory.keys()
        totalAmt = sum(map(lambda x:x.amount, purchaseTransactions))

        for category in mcCategories:
            ctr = {x for x in purchaseTransactions if x.scheme in Constants.FundsByCategory[category]}
            amt = sum(map(lambda z: z.amount, ctr))  
            print(f'{category}: {round(amt,2)} ({round(amt*100/totalAmt, 2)}%)')
        print()

    def calculateTransactionsSummary(adjTransactions):
        print('Adjusting for redemptions,')
        totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE_SIP])
        totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(adjTransactions, [Constants.PURCHASE])
        total = totalSIP + totalLumpSum
        totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(
                            adjTransactions, 
                            [Constants.STAMP_DUTY_TAX, Constants.MISC, Constants.STT_TAX]
                        )
        print(f'Total amount invested through SIPs: {round(totalSIP, 2)} ({round(totalSIP*100/total,2)}%)')
        print(f'Total amount invested through lumpsum: {round(totalLumpSum, 2)} ({round(totalLumpSum*100/total,2)}%)')
        print(f'Total others (stamp duty, transaction charges, redemption STT_Tax): {round(totalStampDuty, 2)}')
        print()

        # Priority
                # currency formatting
                # fetch all long term capital gains eligible purchase transactions
                # print this data in excel
                # add filename arg
                # proper documentation so that no time gone next time
                
                # adding sanity checks
                # testing/ adding checks that csv is correct
        
        # Maybe
                # try and get number of SIPs and their dates and amounts by code
                # SIP chart - x axis shows dates in a month and y shows amount (find way to show which market cap)
                # show graphs in report??
                # get curve of amt invested vs month
                # get a txt report
                # no. of folios by fund
                # print all 3 tables in excel
                # adding args to main.py

        # Done
                # get total amount invested
                # Lumpsum vs SIP
                # top level summary- no. of amc, funds, folios
                # get total amount invested by AMC
                # get total amount invested by scheme
                # get % distribution in LC/MC/SC/L&MC...

                # how to treat redemptions?
                # compare units in folio and scheme subtract from 1st?---> complex
                # sum all except redemption. Rest of the claculation will require manual input
                # have another function for redeemed funds
      
      
       
        
        

       

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
        print('Stamp Duty and other fees have not been included in the below numbers (unless specified.\n')
        purchaseTransactions = {x for x in adjTransactions if x.type in [Constants.PURCHASE, Constants.PURCHASE_SIP, Constants.REVERSAL]}
        
        allAMCs = set(list(map(lambda x: x.amc, purchaseTransactions)))
        allFunds = set(list(map(lambda x: x.scheme, purchaseTransactions)))
        allFolios = set(list(map(lambda x: x.folio, purchaseTransactions)))
        print('Total number of fund houses invested in: ', len(allAMCs))
        print('Total number of funds invested in: ', len(allFunds))
        print('Total number of folios invested in: ', len(allFolios))
        
        for x in allAMCs:
            tr = {z for z in adjTransactions if z.amc==x}
            print()
            amt = sum(map(lambda z: z.amount, tr))
            # print(f'  - {x} : {round(amt,2)}')
            funds = set(list(map(lambda z: z.scheme, tr)))
            # for y in funds:
                # print('    *', y)


        print()
        print('Adjusting for redemptions,')
        totalAmountInvested = sum(map(lambda x: x.amount, purchaseTransactions))
        totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(purchaseTransactions, Constants.PURCHASE_SIP)
        totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(purchaseTransactions, Constants.PURCHASE)
        total = totalSIP + totalLumpSum
        totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(
                            adjTransactions, 
                            [Constants.STAMP_DUTY_TAX, Constants.MISC, Constants.STT_TAX]
                        )
        print('Total amount invested: ', round(totalAmountInvested, 2))
        print('Total amount invested through SIPs: ', round(totalSIP, 2), ' (', round(totalSIP*100/total,2), '% )')
        print('Total amount invested through lumpsum: ', round(totalLumpSum, 2), ' (', round(totalLumpSum*100/total,2),'% )')
        print('Total other (stamp duty, transaction charges, redemption STT_Tax): ', round(totalStampDuty, 3))
        

        # print('Without keeping redemptions in mind,')
        # totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, Constants.PURCHASE_SIP)
        # print('Total amount invested through SIPs is', round(totalSIP, 3))

        # totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, Constants.PURCHASE)
        # print('Total amount invested through lumpsum is', round(totalLumpSum, 3))

        # totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, Constants.STAMP_DUTY_TAX)
        # print('Total stamp duty is', round(totalStampDuty, 3))

        # totalAmountInvested = ReportHelperFunctions.getCurrentTotalAmt(mfTransactions)
        # print('Total amount invested is', round(totalAmountInvested, 3))
        
        # Priority
                # top level summary- no. of amc, funds, folios, folios by fund
                # get total amount invested by scheme
                # get total amount invested by AMC
                # get % distribution in LC/MC/SC/L&MC...
                # print all 3 tables in excel and calculated figures as well
                # get a txt report
                # fetch all long term capital gains purchase transactions
                # adding sanity checks
                # testing/ adding checks that csv is correct
        
        # Maybe
                # try and get number of SIPs and their dates and amounts by code
                # SIP chart - x axis shows dates in a month and y shows amount (find way to show which market cap)
                # show graphs in report??
                # get curve of amt invested vs month
        # Done
                # get total amount invested
                # Lumpsum vs SIP

                # how to treat redemptions?
                # compare units in folio and scheme subtract from 1st?---> complex
                # sum all except redemption. Rest of the claculation will require manual input
                # have another function for redeemed funds
      
      
       
        
        

       

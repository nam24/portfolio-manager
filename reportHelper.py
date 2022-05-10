from dbConstants import Constants
from objects import MFData

class ReportHelperFunctions:
    def getTotalAmountByTransactionType(mfTransactions, type):
        def filterByType(x):
            if(x.type == type):
                return x.amount
            return 0

        return sum(map(filterByType, mfTransactions))
    
    def getCurrentTotalAmt(mfTransactions):
        return sum(map(
                    lambda x: ReportHelperFunctions.getTotalAmountByTransactionType(
                        mfTransactions, 
                        x
                    ), 
                    [
                        Constants.MISC,
                        Constants.PURCHASE_SIP, 
                        Constants.PURCHASE, 
                        Constants.REVERSAL, 
                        Constants.STAMP_DUTY_TAX
                    ]
                ))

    def cleanUpDbObject(mfData):
        # This is to deal with Mirae Assets reporting Refund in one line 
        # instead of 2 (one +ve and one -ve) transactions
        mfTransactions = {x for x in mfData.mfTransactions if "Refund" not in x.description }
    
        return MFData(mfTransactions, mfData.mfInfo, mfData.mfValues)

    def getRedemptionAdjustedTransactions(mfTransactions):
        # To simplify this process, import 'without zero balance folios' from cams
        # Find folios which have redemption
        # for each folio, get total number of units redeemed
        # start subtracting units from increasing date purchase transactions
        # remove transactions which are redeemed fully
        purchaseTransactions = list({x for x in mfTransactions if x.type in [Constants.PURCHASE, Constants.PURCHASE_SIP]})
        redemptionTransactions = {x for x in mfTransactions if x.type == Constants.REDEMPTION}

        for red in redemptionTransactions:
            redUnits = round(red.units, 3) * -1
            # must be sorted in ascending order of date/ transaction
            purchases = list({x for x in purchaseTransactions if x.folio == red.folio and x.scheme == red.scheme})
            purchases = sorted(purchases, key=lambda x:x.transactionDate)
            others = list({x for x in purchaseTransactions if x.folio != red.folio or x.scheme != red.scheme})
            
            while redUnits>0:
                units = round(purchases[0].units,3)
                if(redUnits==units):
                    purchases.pop(0)
                    break
                elif(redUnits<units):
                    purchases[0].units = round(units-redUnits, 3)
                    break
                redUnits = round( redUnits-units, 3)
                purchases.pop(0)

            purchaseTransactions = others + purchases
            # What to do with case where same transaction dates but different NAV dates?
            # For now will assume it taken care of

        others = list({x for x in mfTransactions if x.type not in [Constants.PURCHASE, Constants.PURCHASE_SIP, Constants.REDEMPTION]})

        return purchaseTransactions + others

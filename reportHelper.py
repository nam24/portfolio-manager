from numpy import sort
from dbConstants import DBConstants
from objects import Db, MFTransactions

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
                        DBConstants.MISC,
                        DBConstants.PURCHASE_SIP, 
                        DBConstants.PURCHASE, 
                        DBConstants.REVERSAL, 
                        DBConstants.STAMP_DUTY_TAX
                    ]
                ))

    def cleanUpDbObject(db):
        # This is to deal with Mirae Assets reporting Refund in one line 
        # instead of 2 (one +ve and one -ve) transactions
        mfTransactions = {x for x in db.mfTransactions if "Refund" not in x.description }
    
        return Db(mfTransactions, db.mfInfo, db.mfValues)

    def getRedemptionAdjustedDbObject(db):
        # To simplify this process, import 'without zero balance folios' from cams
        # Find folios which have redemption
        # for each folio, get total number of units redeemed
        # start subtracting units from increasing date purchase transactions
        # remove transactions which are redeemed fully
        mfTransactions = db.mfTransactions
        purchaseTransactions = {x for x in mfTransactions if x.type in [DBConstants.PURCHASE, DBConstants.PURCHASE_SIP]}
        redemptionTransactions = {x for x in mfTransactions if x.type == DBConstants.REDEMPTION}

        for red in redemptionTransactions:
            purchases = {x for x in purchaseTransactions if x.folio == red.folio and x.scheme == red.scheme}
            purchases = list(map(lambda x: x.transactionDate, purchases)) # must be sorted in ascending order
            print(purchases.sort())
            print()
            print()
        # print(redemptionFolios)


        return Db(mfTransactions, db.mfInfo, db.mfValues)

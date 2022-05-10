from dbConstants import DBConstants
from objects import Db

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

    def CleanUpDbObject(db):
        # This arises from Mirae Assets reporting Refund in one line 
        # instead of 2 (one +ve and one -ve) transactions
        mfTransactions = {x for x in db.mfTransactions if "Refund" not in x.description }
    
        return Db(mfTransactions, db.mfInfo, db.mfValues)
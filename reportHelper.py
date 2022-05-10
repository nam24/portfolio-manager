from dbConstants import DBConstants
from objects import MFTransactions

class ReportHelperFunctions:
    def getTotalAmountByTransactionType(mfTransactions, type):
        def filterByType(x):
            # Added for total amt code, so that refund doesn't get added
            # This arises from Mirae Assets reporting Refund in one line 
            # instead of 2 (one +ve and one -ve) transactions
            if(type == DBConstants.MISC):
                if("Refund" in x.description):
                    return 0 
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
                        DBConstants.MISC, # if description contains "Refund", ignore that
                        DBConstants.PURCHASE_SIP, 
                        DBConstants.PURCHASE, 
                        DBConstants.REVERSAL, 
                        DBConstants.STAMP_DUTY_TAX
                        ]
                ))
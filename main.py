from calculateDb import CalculateDb
from dbConstants import DBConstants
from helper import HelperFunctions
from queries import Queries

conn = HelperFunctions.getDbConnectionObject('finance', 'namrata')
cursor = conn.cursor()

db = CalculateDb.calculateDb(conn, 0)

mfTransactions = db.mfTransactions
mfInfo = db.mfInfo # deja vu
mfValues = db.mfValues

# how to treat redemptions?
# compare units in folio and scheme subtract from 1st?---> complex
# sum all except redemption. Rest of the claculation will require manual input
# have another function for redeemed funds
  
totalSIP = HelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.PURCHASE_SIP)
print(totalSIP)

totalLumpSum = HelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.PURCHASE)
print(totalLumpSum)

totalStampDuty = HelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.STAMP_DUTY_TAX)
print(totalStampDuty)

print(HelperFunctions.getCurrentTotalAmt(mfTransactions))

# get total amount invested
# get total amount invested by scheme
# get total amount invested by AMC
# get curve of amt invested vs month
# get % distribution in LC/MC/SC/L&MC...
# Lumpsum vs SIP
# try and get number of SIPs and their dates and amounts by code
# SIP chart - x axis shows dates in a month and y shows amount (find way to show which market cap)

# print all 3 tables in excel and calculated figures as well
# get a txt report
# show graphs in report??
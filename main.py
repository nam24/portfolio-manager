from pickletools import long1
from calculateDb import CalculateDb
from databaseHelper import DatabaseHelperFunctions
from reportHelper import ReportHelperFunctions
from dbConstants import DBConstants
from queries import Queries

conn = DatabaseHelperFunctions.getDbConnectionObject('finance', 'namrata')
cursor = conn.cursor()

db = CalculateDb.calculateDb(conn, 0)
db = ReportHelperFunctions.cleanUpDbObject(db)
mfTransactions = list(db.mfTransactions)
mfInfo = db.mfInfo # deja vu
mfValues = db.mfValues
# adjusting for redemptions
adjTransactions = ReportHelperFunctions.getRedemptionAdjustedTransactions(mfTransactions)

print('Without keeping redemptions in mind,')
totalSIP = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.PURCHASE_SIP)
print('Total amount invested through SIPs is', round(totalSIP, 3))

totalLumpSum = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.PURCHASE)
print('Total amount invested through lumpsum is', round(totalLumpSum, 3))

totalStampDuty = ReportHelperFunctions.getTotalAmountByTransactionType(mfTransactions, DBConstants.STAMP_DUTY_TAX)
print('Total stamp duty is', round(totalStampDuty, 3))

totalAmountInvested = ReportHelperFunctions.getCurrentTotalAmt(mfTransactions)
print('Total amount invested is', round(totalAmountInvested, 3))


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

# how to treat redemptions?
# compare units in folio and scheme subtract from 1st?---> complex
# sum all except redemption. Rest of the claculation will require manual input
# have another function for redeemed funds
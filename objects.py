class MFTransactions:
    def __init__(self, tuple):
        self.amc             = tuple[0] 
        self.folio           = tuple[1] 
        self.scheme          = tuple[2] 
        self.transactionDate = tuple[3] 
        self.description     = tuple[4] 
        self.amount          = tuple[5] 
        self.units           = tuple[6] 
        self.nav             = tuple[7] 
        self.balance         = tuple[8] 
        self.type            = tuple[9] 

class MFInfo:
    def __init__(self, tuple):
        self.amc        = tuple[0]
        self.folio      = tuple[1]
        self.scheme     = tuple[2]
        self.advisor    = tuple[3]
        self.isin       = tuple[4]
        self.amfi       = tuple[5]
        self.dividend   = tuple[6]

class MFValues:
    def __init__(self, tuple):
        self.amc        = tuple[0]
        self.folio      = tuple[1]
        self.registrar  = tuple[2]
        self.scheme     = tuple[3]
        self.open       = tuple[4]
        self.close      = tuple[5]
        self.value      = tuple[6]
        self.date       = tuple[7]

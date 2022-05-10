from dbConstants import Constants

class Queries:
    def dropTableQ(tableName):
        return "DROP TABLE IF EXISTS " + tableName + ";"
    
    def renameColumnsQ(tableName, oldColName, newColName):
        return "ALTER TABLE " + tableName + " RENAME COLUMN " + oldColName + " TO " + newColName + ";"

    def importCSVQ(tableName, targetFileName):
        return "COPY " + tableName + " FROM '" + Constants.filesLocation + targetFileName + "' DELIMITER ',' CSV HEADER;"

    def getAllFromTable(tableName):
        return "select * from " + tableName + ";"
        
    def getAllDisctinctFromTable(tableName):
        return "select distinct * from " + tableName + ";"
    
    def createMFValuesTableQ():
        createTempTableQ = '''
            CREATE TEMPORARY TABLE t2(
                amc VARCHAR(80) NOT NULL,
                folio VARCHAR(25) NOT NULL,
                advisor VARCHAR(40),
                registrar VARCHAR(20),
                pan VARCHAR(10),
                scheme VARCHAR(120),
                isin VARCHAR(15),
                amfi VARCHAR(8),
                open FLOAT8,
                close FLOAT8,
                value FLOAT8,
                date DATE NOT NULL,
                transactions INTEGER
            );
        ''' 
        createMFValuesQ = '''
            CREATE TABLE mfvalues(
                amc VARCHAR(80) NOT NULL,
                folio VARCHAR(25) NOT NULL,
                registrar VARCHAR(20),
                scheme VARCHAR(120),
                open FLOAT8,
                close FLOAT8,
                value FLOAT8,
                date DATE NOT NULL
            );
        ''' 

        populateMFValuesQ = '''
            INSERT INTO mfvalues(amc, folio, registrar, scheme, open, close, value, date)
            SELECT amc, folio, registrar, scheme, open, close, value, date
            FROM t2;
        '''

        Q2 = createTempTableQ + Queries.importCSVQ("t2", "cas-summary.csv")
        Q2 = Q2 + createMFValuesQ
        Q2 = Q2 + populateMFValuesQ
        Q2 = Q2 + Queries.dropTableQ("t2")

        return Q2

    # Main function for creating and populating tables
    # 1. Create a temp table with same schema as the csv files and populate it.
    # 2. Create main tables with required schemas.
    # 3. Populate these tables using temp tables from step 1.
    # 4. Drop the temp table

    def createMFTablesQ():
        createTempTableQ = '''
            CREATE TEMPORARY TABLE t(
                amc VARCHAR(80) NOT NULL,
                folio VARCHAR(25) NOT NULL,
                pan VARCHAR(10),
                scheme VARCHAR(120),
                advisor VARCHAR(40),
                isin VARCHAR(15),
                amfi VARCHAR(8),
                date DATE NOT NULL,
                description TEXT,
                amount FLOAT8 NOT NULL,
                units FLOAT8,
                nav FLOAT8,
                balance FLOAT8,
                type TEXT,
                dividend VARCHAR(10)
            );
        ''' 
        createMFTransactionsQ = '''
            CREATE TABLE mftransactions(
                amc VARCHAR(80) NOT NULL,
                folio VARCHAR(25) NOT NULL,
                scheme VARCHAR(120),
                date DATE NOT NULL,
                description TEXT,
                amount FLOAT8 NOT NULL,
                units FLOAT8,
                nav FLOAT8,
                balance FLOAT8,
                type TEXT
            );
        ''' 
        createMFInfoQ = '''
            CREATE TABLE mfinfo(
                amc VARCHAR(80) NOT NULL,
                folio VARCHAR(25) NOT NULL,
                scheme VARCHAR(120),
                advisor VARCHAR(40),
                isin VARCHAR(15),
                amfi VARCHAR(8),
                dividend VARCHAR(10)
            );
        ''' 

        populateMFTransactionsQ = '''
            INSERT INTO mftransactions(amc, folio, scheme, date, description, amount, units, nav, balance, type)
            SELECT amc, folio, scheme, date, description, amount, units, nav, balance, type
            FROM t;
        '''
        populateMFInfoQ = '''
            INSERT INTO mfinfo(amc, folio, scheme, advisor, isin, amfi, dividend)
            SELECT amc, folio, scheme, advisor, isin, amfi, dividend
            FROM t;
        '''

        Q1 = createTempTableQ + Queries.importCSVQ("t", "cas.csv")
        Q1 = Q1 + createMFTransactionsQ + createMFInfoQ
        Q1 = Q1 + populateMFTransactionsQ + populateMFInfoQ
        Q1 = Q1 + Queries.dropTableQ("t")
        Q2 = Queries.createMFValuesTableQ()

        return Q1 + Q2

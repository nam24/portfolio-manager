class Queries:
    dropTableQ = "DROP TABLE IF EXISTS mftransactions;"
    
    createTableQ = '''
            CREATE TABLE mftransactions(
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
                dividend varchar(10)
            );
        '''

    importCSVQ = "COPY mftransactions FROM '/Users/namrata/Documents/PM/Files/cas.csv' DELIMITER ',' CSV HEADER;"

    getAllMFTransactionsQ = "select * from mftransactions;"


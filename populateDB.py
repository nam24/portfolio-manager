import psycopg2

class PopulateDB:
    def populateMFTransactionsFromCSV():
        #establishing the connection
        conn = psycopg2.connect(
        database="finance", user='namrata', host='127.0.0.1', port= '5432'
        ) # add roles and passwords

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # drop pre-existing table
        dropTableQ = "DROP TABLE IF EXISTS mftransactions;"
        cursor.execute(dropTableQ)

        #create MF transactions table
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
        cursor.execute(createTableQ)

        importCSVQ = "COPY mftransactions FROM '/Users/namrata/Documents/PM/cas.csv' DELIMITER ',' CSV HEADER;"
        cursor.execute(importCSVQ)

        #amc, scheme-name, isin, amfi, pan
        cursor.execute("select * from mftransactions")
        line = cursor.fetchall()
        print(line[0])

        #Closing the connection
        conn.close()
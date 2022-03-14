from dbConstants import DBConstants


class Queries:
    def dropTableQ(tableName):
        return "DROP TABLE IF EXISTS " + tableName + ";"
    
    createMFTransactionsTableQ = '''
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
                dividend VARCHAR(10)
            );
        '''
    
    def renameColumnsQ(tableName, oldColName, newColName):
        return "ALTER TABLE " + tableName + " RENAME COLUMN " + oldColName + " TO " + newColName + ";"

    def importCSVQ(tableName, targetFileName):
        return "COPY " + tableName + " FROM '" + DBConstants.filesLocation + targetFileName + "' DELIMITER ',' CSV HEADER;"

    getAllMFTransactionsQ = "select * from mftransactions;"
'''
create temporary table t (x1 integer, ... , x10 text)
Copy from the file into it:

copy t (x1, ... , x10)
from '/path/to/my_file'
with (format csv)
Now insert into the definitive table from the temp:

insert into my_table (x2, x5, x7, x10)
select x2, x5, x7, x10
from t
And drop it:

drop table t
'''
import sqlalchemy

USER = "root"
PASS = "rootroot"
SERVER = "localhost"
DB_NAME = "anneurism"
ENGINE = sqlalchemy.create_engine('mysql+pymysql://root:rootroot@localhost/anneurism')
TABLE_FIN = "data4"
TABLE_DOUBLE = "doubles"
TABLE_1 = "db1"
TABLE_2 = "db2"
TABLE_3 = "db3"

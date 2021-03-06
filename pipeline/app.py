from sqlalchemy import create_engine
from sql_queries import *
from pathlib import Path

SQLLITEDB1 = 'sqlite:///demo1.db'
SQLLITEDB2 = 'sqlite:///demo2.db'
db1 = create_engine(SQLLITEDB1)
db2 = create_engine(SQLLITEDB2)

def query_db(query, db):
    with db.connect() as con:
        rs = con.execute(query)
    return rs

def initialize_db():
    query_db(CREATE_TBL_A_Q, db1)
    query_db(INSERT_INTO_TBL_A_Q, db1)


if __name__ == '__main__' :
    if not Path(SQLLITEDB1).exists():
        initialize_db()
    
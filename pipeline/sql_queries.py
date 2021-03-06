CREATE_TBL_A_Q = """
CREATE TABLE IF NOT EXISTS table_1 (
  id INTEGER PRIMARY KEY NOT NULL, 
  x REAL NOT NULL,
  y REAL NOT NULL,
  z REAL NOT NULL
);
"""
INSERT_INTO_TBL_A_Q = """
 INSERT INTO table_1
    WITH RECURSIVE
      cnt( id, x, y, z) AS (
      VALUES(1 , random(), random(), random()) UNION ALL 
      SELECT id+1,random(),random(), random() FROM cnt WHERE ID<1000)
    select * from cnt;

 """
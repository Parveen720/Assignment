import sqlite3
conn=sqlite3.connect("db2.db")
conn.execute('''
CREATE TABLE student1(
stid INTEGER PRIMARY KEY AUTOINCREMENT,
stname varchar(255) NOT NULL,
branch varchar(255),
year int)
''')
conn.execute('''
CREATE TABLE employe1(
emid INTEGER PRIMARY KEY AUTOINCREMENT,
emname varchar(255),
Addr varchar(255)
)
''')
conn.execute('''
CREATE TABLE product1(
prid INTEGER PRIMARY KEY AUTOINCREMENT,
prname varchar(255),
prQuantity INT NOT NULL
)
''')
conn.close()
conn.execute('''
INTEGER INTO student1(stname,branch,year) VALUES(
('parveen','AI',2),('riya','AI',2),('yadav','CS','3'))

''')
conn.commit()
conn.execute('''
INTEGER INTO employe1(emname,Addr) VALUES(
('parveen','JAIPUR'),('riya','HANUMANGARH'),('yadav','rewari'))

''')
conn.commit()
conn.execute('''
INTEGER INTO student1(prname,prQuantity) VALUES(
('Soap','10'),('butter','100'),('milk','20'))

''')
conn.commit()
conn.close()


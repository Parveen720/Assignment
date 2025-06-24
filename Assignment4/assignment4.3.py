import sqlite3
conn=sqlite3.connect("db2.db")
conn.execute("DROP TABLE IF EXISTS student1")
conn.execute('''
CREATE TABLE student1(
stid INTEGER PRIMARY KEY AUTOINCREMENT,
stname varchar(255) NOT NULL,
branch varchar(255),
year int)
''')
conn.execute("DROP TABLE IF EXISTS employe1")
conn.execute('''
CREATE TABLE employe1(
emid INTEGER PRIMARY KEY AUTOINCREMENT,
emname varchar(255),
Addr varchar(255)
)
''')
conn.execute("DROP TABLE IF EXISTS product1")
conn.execute('''
CREATE TABLE product1(
prid INTEGER PRIMARY KEY AUTOINCREMENT,
prname varchar(255),
prQuantity INT NOT NULL
)
''')
print("table created succesfully")

conn.execute('''
INSERT INTO student1(stname,branch,year)VALUES
('parveen','AI',2),
('riya','AI',2),
('yadav','CS',3)
''')
conn.execute('''
INSERT INTO employe1(emname,Addr) VALUES
('parveen','JAIPUR'),
('riya','HANUMANGARH'),
('yadav','rewari')

''')
conn.commit()

conn.execute('''
INSERT INTO product1(prname,prQuantity) VALUES
('Soap',10),
('butter',100),
('milk',20)

''')
conn.commit()


data=conn.execute("Select * from student1")
for x in  data:
    print(x)

data=conn.execute("Select * from employe1")
for x in  data:
    print(x)

#for update the values

conn.execute("UPDATE student1 SET stname='hemang' where stid=1")
conn.commit()

#for deleting anything from database

conn.execute("DELETE from student1 where stid=2")
conn.commit()
conn.close()



import sqlite3

conn = sqlite3.connect('C:\\PythonRESTAPITest\\univ.db')

cur = conn.cursor()

#rows = cur.execute('select * from students')

#rows = cur.execute('select studname from students')

rows = cur.execute('select studname from students where city = "New York"')

for t in rows:
    print(t[0])


#print(rows.fetchone())

#print(rows.fetchall())
cur.close()
conn.close()
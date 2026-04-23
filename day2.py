import pymysql
conn=pymysql.connect(host='localhost',
                    user='root', 
                    password='Mahesh@212004')
print("Connection successful")
cursor=conn.cursor()
cursor.execute('use day1')
cursor.execute('select * from schooling')
tables=cursor.fetchall()
print(tables)
for x in tables:
    print(x)
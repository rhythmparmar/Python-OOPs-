import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
if mycon.is_connected()==False:
    print("Error connecting to MySQL database")
cursor=mycon.cursor()
cursor.execute("select*from student")

data=cursor.fetchall()
count=cursor.rowcount
print("Total number of rows retrieved in resultset:",count)
for row in data:
    print(row)

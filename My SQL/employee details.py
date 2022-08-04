import mysql.connector as sqltor

def employee(eid, name,sal):

    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="Insert into emp values({},'{}',{})".format(eid,name,sal)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def display():

    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="select * from emp"
        cursor=mycon.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        print("Employee Details: ")
        for row in data:
            print(row)
    
        mycon.close()    
    
    


n=int(input("Enter total employees: "))

for i in range(n):

    print("Enter Employee details: ")
    eid = int(input("\t Emp ID: "))
    name = input("\t Emp Name: ")
    sal = int(input("\t Emp Salary: "))

    employee(eid,name,sal)
display()

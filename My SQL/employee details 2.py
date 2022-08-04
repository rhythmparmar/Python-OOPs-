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
def remove(eid):

    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="delete from emp where eid={}".format(eid)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def update(eid):

    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:

        name = input("Enter name: ")
        sal = int(input("Enter salary : "))
        sql="update emp set name='{}', salary={} where eid={}".format(name,sal,eid)
        
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def totalEmp():
    count=0
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="select count(*) from emp"
        cursor=mycon.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        if cursor.rowcount==1:
            
            
            count = data[0][0]

        
        mycon.close()
        return count
    
def displayById(eid):

    flag=False
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="select * from emp where eid = {}".format(eid)
        cursor=mycon.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        if cursor.rowcount==1:
            flag=True
            print("Employee Details: ")
            for row in data:
                
                print("{:<5} {:<20} {:<7}".format(row[0],row[1],row[2]))
        else:
            print("Record not found")

        
        mycon.close()
        return flag
    
    
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
            
            print("{:<5} {:<20} {:<7}".format(row[0],row[1],row[2]))
    
        mycon.close()    
    
    

choice=1
while(choice!=6):
    print("-"*20," Menu ","-"*20)
    print("1 - Add Employee")
    print("2 - Remove Employee")
    print("3 - display")
    print("4 - Update")
    print("5 - Total Employees")
    print("6 - Quit")

    choice=int(input("Enter your choice: "))

    print("-"*50)
    if choice==1:
        eid=int(input("Enter Employee Id: "))
        name=input("Enter Employee Name: ")
        sal=int(input("Enter Employee Salary: "))
        employee(eid,name,sal)
    elif choice==2:
        eid=int(input("Enter Employee Id to remove: "))
        remove(eid)
    elif choice==3:
        display()
    elif choice==4:
        eid=int(input("Enter Employee Id to update: "))

         
        if displayById(eid):
            a = int(input("press 1 to update employee : "))
            if(a==1):
                update(eid)
    elif choice==5:
        print("Total Employees : ",totalEmp())
    elif choice==6:
        break
    else:
        print("Error: Invalid choice")



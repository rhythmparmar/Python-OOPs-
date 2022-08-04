import mysql.connector as sqltor


def student(name,rollno,studclass):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")
    else:
        sql="Insert into student values({},'{}',{})".format(rollno,name,studclass)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close
    
 
def remove(rollno):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")
    else:
        sql="delete from student where roll={}".format(rollno)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close
    

def update(rollno):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")
    else:
        sql="update student set name='{}',class={} where rollno={}".format(name,studclass,rollno)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close

def display():
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="test")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
       
        sql="select * from student"
        cursor=mycon.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        print("Student Details: ")
        for row in data:
            
            print("{:<5} {:<20} {:<7}".format(row[0],row[1],row[2]))
    
        mycon.close() 
    
    

choice=1
while(choice!=5):
    print("1 - Add Student")
    print("2 - remove Student")
    print("3 - Update Student")
    print("4 - Display Student")
    print("5 - Quit")

    choice=int(input("Enter Choice: "))

    if(choice==1):
        name=input("Enter Name: ")
        rollno=int(input("Enter Rollno.: "))
        studclass=int(input("Enter Class: "))

    elif choice==2:
        rollno=int(input("Enter rollno to remove: "))
        remove(rollno)

    elif choice==3:
        rollno=int(input("Enter rollno to update: "))
        update(rollno)

    elif choice==4:
        display()

    elif choice==5:
        break
    else:
        print("Error: invalid choice...")

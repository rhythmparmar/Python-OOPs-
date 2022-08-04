import mysql.connector as sqltor

def automobile(Number,model,colour,engine):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="cars")
    if mycon.is_connected()==False:
        print("Error connecting to mysql daatabase")
    else:
        sql="Insert into automobiles values({},'{}','{}','{}')".format(Number,model,colour,engine)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def remove(num):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="cars")
    if mycon.is_connected()==False:
        print("Error connecting to mysql database")
    else:
        sql="delete from automobiles where Number={}".format(num)
        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def update(num):
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="cars")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:

        model=input("Enter New model: ")
        colour=input("Enter New colour: ")
        engine=input("Enter New Engine: ")
        sql="update automobiles set model='{}',colour='{}',engine='{}' where Number={}".format(model,colour,engine,num)

        cursor=mycon.cursor()
        cursor.execute(sql)
        mycon.commit()
        mycon.close()

def display():
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="cars")
    if mycon.is_connected()==False:
        print("Error connecting to MYSQL database")
    else:
        sql="select * from automobiles"
        cursor=mycon.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        print("Automobile Details")
        for row in data:
            print("{:<5} {:<20} {:<7}".format(row[0],row[1],row[2]))

        mycon.close()


choice=1
while(choice!=5):
    print("-"*20,"Menu","-"*20)
    print("1 - Add Vehicle")
    print("2 - Remove vehicle")
    print("3 - Update vehicle")
    print("4 - Display vehicle")
    print("5 - Quit")

    choice=int(input("Enter your choice: "))
    if (choice==1):
        Number=int(input("Enter Number: "))
        model=input("Enter model: ")
        colour=input("Enter colour: ")
        engine=input("Enter Engine: ")
        automobile(Number,model,colour,engine)
    elif (choice==2):
        num=int(input("Enter Number to remove: "))
        remove(num)
    elif (choice==3):
        num=int(input("Enter Number to update: "))
        update(num)
    elif (choice==4):
        display()
    elif (choice==5):
        break
    else:
        print("Error: Invalid choice")
        

import csv

fname="stud.csv"
'''
def init():
    fh=open(fname,"w")
    stuwriter=csv.writer(fh)
    stuwriter.writerow(["Adno.","name","Class","Marks"])
    fh.close()
'''
def addstud():
    fh=open(fname,"a",newline='')
    stuwriter=csv.writer(fh)
    
    print("-"*50)
    print("Enter New Student Record")
    print("-"*50)
    adno=int(input("Enter Admission no.: "))
    name=input("Enter Name: ")
    clas=int(input("Enter Class: "))
    marks=float(input("Enter Marks: "))
    sturec=[adno,name,clas,marks]
    stuwriter.writerow(sturec)
    fh.close()

def displayAll():
    found=False

    try:
        fh=open(fname,"r")
    
        creader=csv.reader(fh)
        print("-"*50)
        print("Adno.\tname\tClass\tMarks")
        print("-"*50)
        for rec in creader:
            for data in rec:
                print(data,"\t",end='')
            found=True
            print()
        fh.close()
        if(found==False):
            print("No record found")
    except:
        print("* No record found")


def displayByClass(c):
    found=False
    
    try:
        fh=open(fname,"r")
    
        creader=csv.reader(fh)
        print("-"*50)
        print("Adno.\tname\tClass\tMarks")
        print("-"*50)
        for rec in creader:
            if rec[2]==c:
                for data in rec:
                    print(data,"\t",end='')
                found=True
                print()

        fh.close()
        if(found==False):
            print("No record found")
    except:
        print("* No record found")
    

def displayByName(a):
    found=False
    
    try:
        fh=open(fname,"r")
    
        creader=csv.reader(fh)
        print("-"*50)
        print("Adno.\tname\tClass\tMarks")
        print("-"*50)
        for rec in creader:
            if rec[1]==a:
                for data in rec:
                    print(data,"\t",end='')
                found=True
                print()

        fh.close()
        if(found==False):
            print("No record found")
    except:
        print("* No record found")

def displayByAdmno(b):
    found=False
    
    try:
        fh=open(fname,"r")
    
        creader=csv.reader(fh)
        print("-"*50)
        print("Adno.\tname\tClass\tMarks")
        print("-"*50)
        for rec in creader:
            if rec[0]==b:
                for data in rec:
                    print(data,"\t",end='')
                found=True
                print()
                break
        fh.close()
        if(found==False):
            print("No record found")
    except:
        print("* No record found")


def avgMarks(c):
    found=False
    
    try:
        fh=open(fname,"r")
    
        creader=csv.reader(fh)
        #print("-"*50)
        #print("Adno.\tname\tClass\tMarks")
        #print("-"*50)
        s=0
        count=0
        print(c)
        for rec in creader:
            if rec[2]==c:
                print(rec[3])
                s=s+float(rec[3])
                count+=1
                #avg=(sum/count)*100
                #print(avg,"\t",end='')
    
                found=True
                #print()

        fh.close()
        if(found==False):
            print("No record found")
        else:
            avg=(s/count)
            print("-"*50)
            print("Average Marks: ",avg)
            print("-"*50)
    except Exception as e:
        print("ERROR: ",e)
    
    
    


#init()
choice=1
while(choice!=5):
    print("1 - Add Student")
    print("2 - DisplayAll")
    print("3 - Display by class")
    print("4 - Display by Name")
    print("5 - Search by Admission No.")
    print("6 - Average Marks of Class: ")
    print("7 - Quit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        addstud()
    elif(choice==2):
        displayAll()
    elif(choice==3):
        c = input("Enter class for search: ")
        displayByClass(c)
    elif (choice==4):
        c = input("Enter name for search: ")
        displayByName(c)
    elif (choice==5):
        c=input("Enter Admission No.: ")
        displayByAdmno(c)
    elif (choice==6):
        c = input("Enter class for search: ")
        avgMarks(c)
    elif(choice==7):
        break
    else:
        print("ERROR:Invalid Choice")
        
        

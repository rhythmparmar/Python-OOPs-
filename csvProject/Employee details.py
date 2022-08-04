import pickle

def searchByDept(c):
    found=False
    empfile=open('emp.dat','rb')

    try:
        while True:
            d=pickle.load(empfile)
            if d['Department']==c:
                print(d)
                found=True
    except EOFError:
        
        if found==False:
            print("data not found")
        
    empfile.close()


d={}
empfile=open('emp.dat','wb')
data='y'
while data=='y':
    empno=int(input("Enter Employee No.: "))
    ename=input("Enter Employee name: ")
    sal=int(input("Enter salary: "))
    dept=int(input("Enter Department No.: "))

    d['EmpNo']=empno
    d['Emp Name']=ename
    d['Salary']=sal
    d['Department']=dept

    pickle.dump(d,empfile)
    data=input("Want to enter more records(y/n)....")
empfile.close()
c=int(input("Enter Department no. to search: "))
searchByDept(c)





    
    

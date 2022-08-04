import pickle
stu={}
stufile=open("stu.dat","wb")
ans="y"
while ans=="y":
    rno=int(input("Enter RollNo.: "))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))

    stu["rollno"]=rno
    stu["name"]=name
    stu["marks"]=marks

    pickle.dump(stu,stufile)
    ans=input("Want to enter more records? (y/n)...")
stufile.close()
    

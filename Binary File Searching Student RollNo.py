import pickle
stu={"12"}
found=False
fin=open("stu.dat","rb")
searchkeys=eval(input("enter roll numbers for searching: "))

try:
    print("Searching in file Stu.dat...")
    while True:
        stu=pickle.load(fin)
        if stu["rollno"] in searchkeys:
            print(stu)
            found=True
except EOFError:
    if found==False:
        print("No such records found in the file")
    else:
        print("Search Successful.")
    fin.close()

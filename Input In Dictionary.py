d={}
n=int(input("Enter total students: "))
for i in range(n):
    roll=int(input("Enter Roll.No: "))
    name=input("Enter Name: ")
    d[roll]=name
print("R.No. \t Name")

for i in d:
    print(i,"\t",d[i])

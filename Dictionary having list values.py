d={}
n=int(input("Enter total Students: "))
for i in range(n):
    roll=int(input("Enter Roll No.: "))
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    d[roll]=[name,marks]
print("R.No \t Name \t Marks")

for i in d:
    print(i,"\t",d[i][0],"\t",d[i][1])

d={}
n=int(input("Enter total Students: "))
for i in range(n):
    roll=int(input("Enter Roll No.: "))
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    d[roll]=[name,marks]

top_key=0
for k in d:
    if top_key==0:
        top_key=k
        continue
    if(d[k][1]>[top_key][1])
    top_key=key
print()
    
print("R.No \t Name \t Marks")

for i in d:
    print(i,"\t",d[i][0],"\t",d[i][1])
    


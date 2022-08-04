'''n=int(input("Enter value of n: "))
d={}
for i in range(n):
    name=input("Enter Name: ")
    if name in d:
        d[name]=d[name]+1
    else:
        d[name]=1


print("name \t Occurance")
for i in d:
    print(i,"\t",d[i])'''


n=int(input("Enter value of n: "))
d=[]
for i in range(n):
    name=input("Enter Name: ")
    
    d.append(name)

d.sort()
print("name \t Occurance")
i=0
while(i<len(d)):
    c=d.count(d[i])
    print(d[i],'\t',c)
    i=i+c


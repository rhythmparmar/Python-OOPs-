L=[]
n=int(input("Enter Number:"))

for i in range(n):
    val=int(input("Enter Element:"))
    L.append(val)
print("Index \t value")

for i in range(len(L)):
    print(i,"\t",L[i])

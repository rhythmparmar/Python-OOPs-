L=[1,6,9,16,33,59,2]
for i in range(1,len(L)):
    for j in range(0,len(L)-i):
        if(L[j]>L[j+1]):
            L[j],L[j+1]=L[j+1],L[j]
print("Sorted List: ",L)

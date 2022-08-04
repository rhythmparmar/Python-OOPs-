L=[34,11,27,85,45,39]

for i in range(0,len(L)-1):
    for j in range(i+1,len(L)):
        if(L[i]>L[j]):
            L[i],L[j]=L[j],L[i]
print("Sorted List: ",L)

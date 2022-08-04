L=[3,7,12,45,77,90,1]
s=int(input("Enter Element to search:"))
for i in range(len(L)):
    if(L[i]==s):
        print("Element found at index:",i)
        break
else:
    print("Element Not found")

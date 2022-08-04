# array must br sorted in binary search.

L=[1,12,34,56,78,90]
s=int(input("Enter number to be searched:"))

beg,end=0,len(L)-1
while(beg<=end):
    mid=(beg+end)//2
    if(L[mid]==s):
        print("Element found at index:",mid)
        break
    if(s<L[mid]):
        end=mid-1
    else:
        beg=mid+1
else:
    print("Element not found")

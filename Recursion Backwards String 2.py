def back(s,n):
    if(n>0):
        k=len(s)-n
        back(s,n-1)
        print(s[k],end="")
    elif n==0:
        return

s=input("Enter String: ")
back(s,len(s))

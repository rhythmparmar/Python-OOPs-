def back(s,n):
    if (n>0):
        print(s[n],end="")
        back(s,n-1)
    elif (n==0):
        print(s[0])

s=input("Enter String: ")
back(s,len(s)-1)

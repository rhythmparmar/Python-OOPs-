n=int(input("Enter Number: "))
s=0
i=n
while(i>0):
    r=i%10
    s=s+r
    i=i//10
print("Sum of Digits of",n,"is",s)

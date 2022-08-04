def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))

a=4
f=factorial(a)
print("Factorial of ",a,"is",f)

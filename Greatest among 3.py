n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number"))
n3=int(input("Enter Third number"))

if (n1>n2) and (n1>n3):
    print(n1,"is Greater")
elif (n2>n1) and (n2>n3):
    print(n2,"is Greater")
else:
    print(n3,"is Greater")

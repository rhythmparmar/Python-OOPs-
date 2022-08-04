filename = input("Enter file name: ")
n=int(input("Enter n: "))
try:
    f = open(filename,'r')
    print("Method 1")
    for l in f:
        print(l.strip())
    f.close()

    print("Method 2")
    f = open(filename,'r')
    str=" "
    while str:
        str = f.readline(n)
        print(str.strip())
    f.close()

    print("Method 3")
    f = open(filename,'r')
    str= f.readlines()
    print(str)
    for i in str:
        print(i.strip())
    f.close()    
except FileNotFoundError:
    print("ERROR: please enter valid file name")


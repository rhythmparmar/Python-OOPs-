filename = input("Enter file name: ")
n = int(input("Enter number of characters to be read:"))

try:
    f = open(filename,'r')

    s = f.read(n)
    print(s)
    f.close()
except FileNotFoundError:
    print("ERROR: please enter valid file name")

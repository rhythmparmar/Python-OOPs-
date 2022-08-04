
stud=['1 Ram 90\n','2 Mohan 89']
try:
    filename = input("Enter file name: ")
    f = open(filename,'w')
    f.writelines(stud)
    print("data stored successfully...")
    f.close()

    print("Method 2")

    filename = input("Enter file name: ")
    f = open(filename,'w')
    n = int(input("Enter total lines: "))
    for i in range(n):
        s = input()
        f.write(s+"\n")
    f.close()
    print("data stored successfully...")
except FileNotFoundError:
    print("ERROR: please enter valid file name")



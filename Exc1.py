n1 = int(input("Enter Divident: "))
n2 = int(input("Enter Divisor: "))

try:
    n3 = n1/n2
    print(n3)
except:
    print("ERROR: Division by Zero not allowed")

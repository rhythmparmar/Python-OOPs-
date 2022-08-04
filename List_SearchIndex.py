L=[1,2,4,6,32,123]

val = int(input("Enter element whose index is required: "))

if val in L:
    print("Item found at index : " ,L.index(val))
else:
    print("Not Found")

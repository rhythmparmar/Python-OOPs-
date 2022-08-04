L=[23,1,45,2,1,56,32]

choice = input("A for Ascending, D for Descending : ")

if(choice=='A'):
    L.sort(reverse=False)
    print(L)
else:
    L.sort(reverse=True)
    print(L)

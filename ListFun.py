L=[12,3,4,5,6,7,123,43,21,1,2,3,1,2]

print("Length of List: ",len(L))
print("Maximum Element of List: ",max(L))
print("Minimum Element of List: ",min(L))
print("Sum of List: ",sum(L))

print("Occurence of 1 in List : ",L.count(1))
print("Occurence of 11 in List : ",L.count(11))

print("Remove last element of list : ",L.pop())
print("Modified List : ",L)

print("Remove 3 element of list : ",L.pop(2))
print("Modified List : ",L)

L1=[10,20]
L.append(L1)

print("Modified List after append : ",L)

print("Last Element of List : ",L[-1])

L.extend(L1)

print("Modified List after extend : ",L)

L.extend("INDIA")

print("Modified List after extend : ",L)

L.insert(2,22) #if index does not exist than it will add at last position

print("Modified List after insert 22 at index 2 : ",L)

#remove 4 element from list without pop()
del L[3]
print("Modified List : ",L)
#remove list from memory

del L

print("After list delete : ",L)

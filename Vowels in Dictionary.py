#d={'a':0,'e':0,'i':0,'o':0,'u':0}
k=['a','e','i','o','u']
d=dict.fromkeys(k,0)
s=input("Enter String: ")
for i in s:
    if i in d:
        d[i]=d[i]+1
print("Vowel \t Occ")
for k in d:
    print(k,"\t",d[k])
    


# use of zip function

k=['a','e','i','o','u']
v=[1,2,3,4,5]

d1 = dict(zip(k,v))
print(d1)

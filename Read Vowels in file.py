fname=input("Enter file name: ")
f=open(fname,"r")
count=0
L=f.readlines()
print(L)
lines=len(L)
f.seek(0)
str=f.read()
for ch in str:
    if(ch=="A" or ch=="a" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u"):
        count=count+1

f.close()
print(lines)
print(count)



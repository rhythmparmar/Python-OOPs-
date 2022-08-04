def compute(num):
    if(num==1):
        return 1
    else:
        return(num+compute(num-1))

last=4
sum=compute(last)
print("Sum of numbers is: ",sum)

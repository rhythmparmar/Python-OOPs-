'''
c=lambda a:a+10      # lambda argument:expression
print(c(5))
'''

'''
x=lambda a,b,c:a+b+c
print(x(3,8,5))
'''


'''
str="Python For Python"
print(lambda str:b)
'''


'''
cube=lambda a:a*a*a
print(cube(2))
'''


'''
tables=[lambda x=x:x*10 for x in range(1,11)]      #prints table of 10
for x in tables:
    print(x())
'''


'''
nmax=lambda a,b:a if(a>b) else b
print(max(64,92))
'''


'''
List=[[2,3,4],[5,2,8,69],[3,7,8,33]]
sortList=lambda x:(sorted(i)for i in x)

secondLargest=lambda x,f:[y[len(y)-2] for y in f(x)]
res=secondLargest(List,sortList)

print(res)
'''









































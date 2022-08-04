class NegNumberException(Exception):
    def __init__(self,msg="ERROR Occured"):
        self.msg=msg

    def __str__(self):
        return self.msg


n=int(input("Enter Number: "))
try:
    if (n<0):
        raise NegNumberException("ERROR: -ve number not allowed")
    
    '''b=10/0
    L=[2,3]
    print(b)'''
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial of",n,"is: ",f)
except NegNumberException as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
except:
    print("ERROR: occured")
else:
    print("Everything is fine")
finally:
    print("I will execute ")
    

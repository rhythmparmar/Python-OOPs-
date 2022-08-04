class NegNumberException(Exception):
    def __init__(self,msg="ERROR Occured"):
        self.msg=msg

    def __str__(self):
        return self.msg+"-> Rhythm"

n=int(input("Enter Number: "))

try:
    if n<0:
        raise NegNumberException("ERROR: -ve number not allowed")
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial of",n,"is: ",f)
except NegNumberException as e:
    print(e)
    

class OutOfBoundException(Exception):
    def __init__(self,msg="Khatarnak Error Occured"):
        self.msg=msg

    def __str__(self):
        return self.msg



n1=int(input("Enter First Number: "))
n2=int(nput("Enter Decond Number: "))

try:
    if(n1<0) and (n2>100):
        raise OutOfBoundException("Error: Input value out of bound")
        
    n3=n1*n2
    print(n1,"X",n2,"=",n3)

except OutOfBoundexception as s:
    print(s)

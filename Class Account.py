class AccountException(Exception):
    def __init__(self,msg="Error Occurred"):
        self.msg=msg
    def __str__(self):
        return self.msg



class Account:
    def __init__(self):
        self.accno=0
        self.name=''
        self.balance=0
        
    def get(self):
        self.accno=int(input("Enter Account no.: "))
        self.name=input("Enter Name: ")
        self.balance=int(input("Enter Balance: "))
    

    def display(self):
        print("Account No.: ",self.accno)
        print("Name: ",self.name)
        print("Balance: ",self.balance)


    def deposit(self,n):
        try:
            if (n<=0):
                raise AccountException("Error: -ve Deposit value Entered")
            self.balance=self.balance+n
        except AccountException as e:
            print(e)


    def withdrawl(self,n):
        try:
            if(n<=0):
                raise AccountException("Error: -ve Withdrawl value Entered")
            self.balance=self.balance-n
        except AccountException as e:
            print(e)
            
            
a1=Account()
a1.get()
choice=1
while(choice!=4):
    print("1 - Deposit")
    print("2 - Withdrawl")
    print("3 - Display")
    print("4 - Quit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        amt=int(input("Enter Deposit Amount: "))
        a1.deposit(amt)
    elif choice==2:
        amt=int(input("Enter Withdrawl Amount: "))
        a1.withdrawl(amt)
    elif choice==3:
        a1.display()
    elif choice==4:
        break
    else:
        print("Error: Invalid choice")
        
     

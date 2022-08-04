class Time:
    count=7
    
    def __init__(self):      #Constructor
        self.hrs=0           #instance Varibale
        self.min=0            #instance Varibale
        self.sec=0             #instance Varibale

    def getTime(self):
        self.hrs=int(input("Enter hours: "))
        self.min=int(input("Enter minutes: "))
        self.sec=int(input("Enter seconds: "))
        self.validate()

    def display(self):
        print(self.hrs,":",self.min,":",self.sec)
        print("count =",Time.count)
        Time.count=10

    def validate(self):
        if(self.sec>=60):
            self.min=self.min+self.sec//60
            self.sec=self.sec%60
        if(self.min>=60):
            self.hrs=self.hrs+self.min//60
            self.min=self.min%60

t1=Time()
t2=Time()
t1.getTime()
t2.getTime()
t1.display()
t2.display()

class Employee:
    def get(self):
        self.id=int(input("Enter id: "))
        self.name=input("Enter name: ")
        self.basic=int(input("Enter basic: "))

        self.calculate()

    def calculate(self):
        self.da=(33*self.basic)/100
        self.hra=(30*self.basic)/100
        self.gross=self.basic+self.hra+self.da
        self.tax=(15*self.gross)/100
        self.net=self.gross-self.tax

    def display(self):
        print("id: ",self.id)
        print("Name: ",self.name)
        print("Basic: ",self.basic)
        print("da: ",self.da)
        print("hra: ",self.hra)
        print("gross: ",self.gross)
        print("tax: ",self.tax)
        print("net: ",self.net)

e1=Employee()

e1.get()

e1.display()
        
        

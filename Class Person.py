class Person:
    def __init__(self):
        self.id=0
        self.name=''
        
    def get(self):
        self.id=int(input("Enter id: "))
        self.name=input("Enter name: ")

    def display(self):
        print("Id: ",self.id)
        print("Name: ",self.name)

class Employee(Person): #Parent class- Person
    def __init__(self):
        super().__init__()
        self.salary=0

    def get(self):
        super().get()
        self.salary=int(input("Enter Salary: "))

    def display(self):
        super().display()
        print("Salary: ",self.salary)
        

e1 = Employee()
e1.get()
e1.display()

'''
p1=Person()
p2=Person()

p1.get()
p2.get()

p1.display()
p2.display()
        
'''

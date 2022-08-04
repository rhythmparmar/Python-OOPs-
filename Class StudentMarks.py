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

class Student(Person):
    def __init__(self):
        super().__init__()
        self.marks=0

    def get(self):
        super().get()
        self.marks=[]
        n=int(input("Enter Number: "))
        for i in range(n):
            val=int(input("Enter Elements: "))
            marks.append(val)


    def display(self):
        super().display()
        for i in range(len(marks)):
            print(L[i])

s1=Student()
s2=Student()

s1.get()
s2.get()

s1.display()
s2.display()

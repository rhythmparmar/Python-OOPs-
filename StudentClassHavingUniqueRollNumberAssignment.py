class Student:
    count=0  #class variable

    def __init__(self):
        Student.count=Student.count+1
        self.roll = Student.count
        
    def get(self):
        #self.roll=int(input("Enter Roll No.: "))
        self.name=input("Enter name: ")     #Instance Variable
        self.marks=int(input("Enter marks: ")) #Instance Variable

    def display(self):
        print("Roll No.: ",self.roll)
        print("Name: ",self.name)
        print("Marks: ",self.marks)

s1=Student()
s2=Student()

s1.get()
s2.get()

s1.display()
s2.display()
        
        

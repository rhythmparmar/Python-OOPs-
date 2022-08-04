class Student:
    def get(self):
        self.roll=int(input("Enter Roll No.: "))
        self.name=input("Enter name: ")
        self.marks=int(input("Enter marks: "))

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
        
        

class Employee:
    def get(self):
        self.id=int(input("Enter id: "))
        self.name=input("Enter Name: ")
        self.age=int(input("Enter age: "))
        self.occupation=input("Enter Occupation: ")

    def display(self):
        print("id: ",self.id)
        print("name: ",self.name)
        print("age: ",self.age)
        print("Occupation: ",self.occupation)

e1=Employee()
e2=Employee()

e1.get()
e2.get()

e1.display()
e2.display()

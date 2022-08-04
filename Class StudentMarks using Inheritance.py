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
    sub=['Maths', 'Hindi','English','Science','SST']
    def __init__(self):
        super().__init__()
        self.marks=[]

    def get(self):
        super().get()

        print("Enter Marks: ")
        for i in range(5):
            s=Student.sub[i]+": "
            val=int(input(s))
            self.marks.append(val)
        self.calculate()
        self.grade()
        


    def display(self):
        super().display()

        print("Subject \t Marks")
        for i in range(len(self.marks)):
            print(Student.sub[i],"\t",self.marks[i])
        print("Percentage: ",self.per)
        print("Grade: ",self.grade)

    def calculate(self):
        sum = 0
        for i in range(5):
            sum+=self.marks[i]
        self.per = (sum*100)/500
        

    def grade(self):
            if self.per>80 and self.per<=100:
                self.grade="A"
                
            if self.per>70 and self.per<=80:
                self.grade="B"
                
            if self.per>50 and self.per<=70:
                self.grade="C"
                
            if self.per>30 and self.per<=50:
                self.grade="D"
                
            else:
                self.grade="E"
            
                


s1=Student()
#s2=Student()

s1.get()
#s2.get()

s1.display()
#s2.display()

class Publication:
    def __init__(self):
        self.title=''
        self.price=0

    def get(self):
        self.title=input("Enter Title: ")
        self.price=float(input("Enter Price: $"))

    def display(self):
        print("Title: ",self.title)
        print("Price: ",self.price)

class Book(Publication):
    def __init__(self):
        super().__init__()
        self.pagecount=0

    def get(self):
        super().get()
        self.pagecount=int(input("Enter Page Count: "))

    def display(self):
        super().display()
        print("Page Count: ",self.pagecount)

class Tape(Book):
    def __init__(self):
        super().__init__()
        self.palytime=0

    def get(self):
        super().get()
        self.playingtime=float(input("Enter minutes played: "))

    def display(self):
        super().display()
        print("Minutes played: ",self.playingtime,"minutes")


p1=Tape()
p1.get()
p1.display()

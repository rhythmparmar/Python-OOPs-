from tkinter import *
root=Tk()
root.geometry("600x600")

class Table():

    def __init__(self,root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e=Entry(root,width=20,fg="blue",
                             font=("lucida calligaraphy",16,"bold"))

                self.e.grid(row=i,column=j)
                self.e.insert(END,lst[i][j])

# take the data
lst=[(1,"Raj","Mumbai",19),
     (2,"AAryan","pune",18),
     (3,"Ramesh","Mumbai",20),
     (4,"Vivek","Mumbai",21),
     (5,"Shubham","Delhi",21),]

total_rows=len(lst)
total_columns=len(lst[0])

t=Table(root)

root.mainloop()


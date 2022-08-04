from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
root=Tk()
root.geometry("500x600")

num_var=IntVar()

def numType():
    if num_var.get()%2==0:
        msg=str(num_var.get())+" is Even"

    else:
        msg=str(num_var.get())+" is Odd"

    print(showinfo("Result", msg))


def fact():
    f=1
    for i in range(1,num_var.get()+1):
        f=f*i
    print(showinfo("Result",f))
        
        
def quit():
    print(showinfo("Maths Example","Bye Bye"))
    root.destroy
    


menu_bar=Menu(root)

maths=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Maths",menu=maths)
maths.add_command(label="Even/Odd",command=numType)
maths.add_command(label="Fact",command=fact)
maths.add_separator()
maths.add_command(label="Exit",command=quit)

num_label=Label(root,text="Number: ",font=("lucida calligraphy",10,"bold"))
num_entry=Entry(root,textvariable=num_var,font=("lucida calligraphy",10,"normal"))

root.config(menu=menu_bar)
num_label.grid(row=0,column=0)
num_entry.grid(row=0,column=1)


root.mainloop()





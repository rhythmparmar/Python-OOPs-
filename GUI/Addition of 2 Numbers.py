from tkinter import *

root=Tk()

root.geometry("800x800")

number1_var=IntVar()
number2_var=IntVar()
result_var=IntVar()


def add():
    num1=number1_var.get()
    num2=number2_var.get()
    print("Number 1 is: "+str(num1))
    print("Number 2 is: "+str(num2))

    num3=num1+num2
    result_var.set(num3)
    print(num3)

def sub():
    num1=number1_var.get()
    num2=number2_var.get()
    print("Number 1 is: "+str(num1))
    print("Number 2 is: "+str(num2))

    num3=num1-num2
    result_var.set(num3)

def mul():
    num1=number1_var.get()
    num2=number2_var.get()
    print("Number 1 is: "+str(num1))
    print("Number 2 is: "+str(num2))

    num3=num1*num2
    result_var.set(num3)

def div():
    num1=number1_var.get()
    num2=number2_var.get()
    print("Number 1 is: "+str(num1))
    print("Number 2 is: "+str(num2))

    num3=num1//num2
    result_var.set(num3)

def rem():
    num1=number1_var.get()
    num2=number2_var.get()
    print("Number 1 is: "+str(num1))
    print("Number 2 is: "+str(num2))

    num3=num1%num2
    result_var.set(num3)



number1_label=Label(root,text="Number 1",font=("calibre",10,"bold"))
number1_entry=Entry(root,textvariable=number1_var,font=("calibre",10,"normal"))

number2_label=Label(root,text="Number 2",font=("calibre",10,"bold"))
number2_entry=Entry(root,textvariable=number2_var,font=("calibre",10,"normal"))

result_label=Label(root,text="Result",font=("calibre",10,"bold"))
result_entry=Entry(root,textvariable=result_var,font=("calibre",10,"normal"))


sub_btn1=Button(root,text="Addition",command=add)
sub_btn2=Button(root,text="Subtraction",command=sub)
sub_btn3=Button(root,text="Multiplication",command=mul)
sub_btn4=Button(root,text="Division",command=div)
sub_btn5=Button(root,text="Remainder",command=rem)

number1_label.grid(row=0,column=0)
number1_entry.grid(row=0,column=1)
number2_label.grid(row=1,column=0)
number2_entry.grid(row=1,column=1)
sub_btn1.grid(row=2,column=0)
sub_btn2.grid(row=2,column=1)
sub_btn3.grid(row=3,column=0)
sub_btn4.grid(row=3,column=1)
sub_btn5.grid(row=4,column=0)
result_label.grid(row=5,column=0)
result_entry.grid(row=5,column=1)
root.mainloop()


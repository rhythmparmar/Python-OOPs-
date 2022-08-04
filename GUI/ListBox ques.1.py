from tkinter import *
root=Tk()
root.geometry("600x800")

def valueRightShift():
    list_box2.insert(0,list_box1.get(ANCHOR))
    list_box1.delete(ANCHOR)

def valueLeftShift():
    list_box1.insert(0,list_box2.get(ANCHOR))
    list_box2.delete(ANCHOR)
    

    
list_box1=Listbox(root,height=10,width=15,bg="yellow",
                  font="Helvetica",fg="red")
list_box2=Listbox(root,height=10,width=15,bg="blue",
                  font="Helvetica",fg="red")


list_box1.insert(1,"A")
list_box1.insert(2,"B")
list_box1.insert(3,"C")
list_box1.insert(4,"D")

btn1=Button(root,text=">>",command=valueRightShift)
btn2=Button(root,text="<<",command=valueLeftShift)

list_box1.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=1,column=1)
list_box2.grid(row=0,column=2)

root.mainloop()

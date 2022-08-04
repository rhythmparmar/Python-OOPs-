from tkinter import *
root=Tk()
root.geometry("600x800")
root.title("ListBox")

# Create List Box
list_box=Listbox(root,height=10,width=15,bg="yellow",
                 font="Helvetica",fg="red")

label=Label(root,text="Food Items: ")

# Insert elements by their index and names
list_box.insert(1,"nachos")
list_box.insert(2,"sandwich")
list_box.insert(3,"burger")
list_box.insert(4,"Pizza")
list_box.insert(5,"Burrito")

# Deleting element by thier index
list_box.delete(2)

label.grid(row=0,column=0)
list_box.grid(row=0,column=1)

root.mainloop()

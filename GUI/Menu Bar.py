from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
root=Tk()
root.title("MenuBar")
root.geometry("600x5000")

def quit():
    print(showinfo("My Menu Example", "Thanks for visiting"))
    root.destroy
# creating Menu Bar
menu_bar=Menu(root)

# Adding File menu and commands
file=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File",commmand=None)
file.add_command(label="Open...",command=None)
file.add_command(label="Save",command=None)
file.add_separator()
file.add_command(label="Exit",command=quit)

# Adding Edit menu and commands
edit=Menu(menu_bar,tearoff = 0)
menu_bar.add_cascade(label ='Edit',menu=edit)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label='Select All',command=None)
edit.add_separator()
edit.add_command(label='Find...',command=None)
edit.add_command(label='Find again',command=None)

# Adding Help menu
help_=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_)
help_.add_command(label="Tk Help",command=None)
help_.add_command(label="Demo",command=None)
help_.add_separator()
help_.add_command(label="About Tk",command=None)

# display Menu
root.config(menu=menu_bar)

root.mainloop()

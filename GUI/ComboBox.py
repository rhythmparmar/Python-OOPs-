from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("ComboBox")
window.geometry("500x250")


def selectedValue():
    print(n.get())
# label text for title
Label(window,text="GFG Combobox Widget",
      background="green",foreground="white",
      font=("Times New Roman",15)).grid(row=0,column=1)

# label
Label(window,text="select the Month: ",
      font=("Times New Roman",10)).grid(column=0,
      row=5,padx=10,pady=25)

# Combobox Creation
n=StringVar()
monthchoosen=Combobox(window, width=27, textvariable=n)
btn=Button(window, text="submit",command=selectedValue)



#  Adding combobox drop down list
monthchoosen["values"]=("January",
                        "february",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "october",
                        "November",
                        "December")

monthchoosen.grid(column=1,row=5)
btn.grid(column=2,row=5)
monthchoosen.current(1)
window.mainloop()

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title("Shopping Mart")
root.geometry("700x600")

radio_var=StringVar()
coupon_var=StringVar()
checkbutton1=IntVar()
checkbutton2=IntVar()
checkbutton3=IntVar()
combobox1=IntVar()
combobox2=IntVar()
combobox3=IntVar()
amount_var=IntVar()
less_discount_var=IntVar()
net_payable_var=IntVar()
less_coupon_var=IntVar()
bill_amount_var=IntVar()


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()
 
    # opens the image
    img = Image.open(x)
     
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 1000), Image.ANTIALIAS)
 
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
  
    # create a label
    panel = Label(root, image = img)
     
    # set the image as img
    panel.image = img
    panel.grid(row = 2)

chitkara_label=Label(root,text="CHITKARA SHOPPING MART",font=("lucida calligraphy",20,"bold")).grid(row=1,column=1)
payment_label=Label(root,text="Payment Method",font=("lucida calligraphy",10,"bold")).grid(row=2,column=0)
r1=Radiobutton(root,text="CDD",variable=radio_var,value="CDD").grid(row=4,column=0)
r2=Radiobutton(root,text="DC/CC(2% discount)",variable=radio_var,value="DC/CC").grid(row=5,column=0)
r3=Radiobutton(root,text="wallet(5% discount)",variable=radio_var,value="wallet").grid(row=6,column=0)
coupon_label=Label(root,text="Coupon",font=("lucida calligraphy",10,"bold")).grid(row=7,column=0)
coupon_entry=Entry(root,textvariable=coupon_var,font=("lucida calligraphy",10,"normal")).grid(row=7,column=1)


check_btn1=Checkbutton(root,text="Pen",variable=checkbutton1,
                    onvalue=1,offvalue=0,width=10).grid(row=8,column=0)

check_btn2=Checkbutton(root,text="Notebook",variable=checkbutton2,
                    onvalue=1,offvalue=0,width=10).grid(row=9,column=0)

check_btn3=Checkbutton(root,text="Rubber",variable=checkbutton3,
                    onvalue=1,offvalue=0,width=10).grid(row=10,column=0)


combo_box1=Combobox(root, width=27, textvariable=combobox1)
combo_box1.grid(row=8,column=1)
combo_box2=Combobox(root, width=27, textvariable=combobox2)
combo_box2.grid(row=9,column=1)
combo_box3=Combobox(root, width=27, textvariable=combobox3)
combo_box3.grid(row=10,column=1)

combo_box1["values"]=("1","2","3")
combo_box2["values"]=("1","2","3")
combo_box3["values"]=("1","2","3")

submit_btn=Button(root,text="Submit")

billing_details_label=Label(root,text="Billing Details",font=("lucida calligraphy",10,"bold")).grid(row=11,column=0)
amount_label=Label(root,text="Amount",font=("lucida calligraphy",10,"bold")).grid(row=12,column=0)
amount_entry=Entry(root,textvariable=amount_var,font=("lucida calligraphy",10,"normal")).grid(row=12,column=1)
less_discount_label=Label(root,text="Less:Discount",font=("lucida calligraphy",10,"bold")).grid(row=13,column=0)
less_discount_entry=Entry(root,textvariable=less_discount_var,font=("lucida calligraphy",10,"normal")).grid(row=13,column=1)
net_payable_label=Label(root,text="Net payable",font=("lucida calligraphy",10,"bold")).grid(row=14,column=0)
net_payable_entry=Entry(root,textvariable=net_payable_var,font=("lucida calligraphy",10,"normal")).grid(row=14,column=1)
less_coupon_label=Label(root,text="Less:Coupon",font=("lucida calligraphy",10,"bold")).grid(row=15,column=0)
less_coupon_entry=Entry(root,textvariable=less_coupon_var,font=("lucida calligraphy",10,"normal")).grid(row=15,column=1)
bill_amount=Label(root,text="Bill Amount",font=("lucida calligraphy",10,"bold")).grid(row=16,column=0)
bill_amount=Entry(root,textvariable=bill_amount_var,font=("lucida calligraphy",10,"normal")).grid(row=16,column=1)

submit_btn.grid(row=17,column=0)



root.mainloop()





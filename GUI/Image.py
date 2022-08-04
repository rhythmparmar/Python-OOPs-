from tkinter import *

# loading python Imaging Library
from PIL import ImageTk,Image

# To get the dialog box to open when required
from tkinter import filedialog

def open_img():
    # Select the Imagename  from a folder
    x = openfilename()
 
    # opens the image
    img = Image.open(x)
     
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
 
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
  
    # create a label
    panel = Label(root, image = img)
     
    # set the image as img
    panel.image = img
    panel.grid(row = 2)

def openfilename():

    # open file dialog box to select image
    # The dialog box has a title "Open"

    filename=filedialog.askopenfilename(title="open")
    return filename


root=Tk()
root.title("Image Loader")
root.geometry("550x600")
root.resizable(width=True,height=True)

btn=Button(root,text="Open image",command=open_img).grid(row=1,columnspan=4)




root.mainloop()

'''
from tkinter import *
root = Tk()
root.geometry("1080x1920")
photo = PhotoImage(file="bhola.png")
varun_label = Label(image=photo)
varun_label.grid(row=0,column=0)
root.mainloop()
'''

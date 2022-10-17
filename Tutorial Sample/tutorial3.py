from tkinter import *
from PIL import Image, ImageTk
import os

def import_photo():
    global var
    print("Importing Photo...")
    #file = str(os.getcwd()) + var.get() + '.png'
    file = 'C:\Users\YWFU\Documents\Github\EGL314starterkit\Tutorial Sample\' + var.get() + '.png'
    print("Image is {}".format(file))
    myImage = Image.open(file)
    myImage.show()


# Main GUI Windows
main = Tk()
main.title('Tutorial 3 Sample')

# Import Photo Section
title = Label(main, text="Import Photo Here:", font=(80))
title.grid(row=0, column=0)

var = StringVar(); 
input = Entry(main, textvariable= var, font=(80))
input.grid(row=0, column=1)

submit = Button(main, text="Import", font=(80), command=import_photo)
submit.grid(row=0, column=2)


main.mainloop()
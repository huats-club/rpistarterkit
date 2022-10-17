from tkinter import *
from PIL import Image
import os

def import_photo():
    global var
    print("Importing Photo...")
    
    choice = var.get()

    # if user did not input any text
    if len(choice) == 0:
        path = os.path.abspath('images') + '\\' + 'cat.png'
        file = path.replace('\\','/')
        myImage = Image.open(file)
        myImage.show()
    # if user input ball, cat or dog
    else:
        path = os.path.abspath('images') +'\\' + var.get() + '.png'
        file = path.replace('\\','/')
        print("file path is {}".format(file))
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
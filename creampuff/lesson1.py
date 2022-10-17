from tkinter import *
from tkinter import messagebox

def button_pressed():
    print("Kena Pressed!!!!")
    messagebox.showinfo( "Sold out liao", "Eh sorry, curry puff sold out.")

main = Tk()
main.title('Curry Puff')

title = Label(main, text="Welcome to my curry puff shop!!!", font=(8000))
title.grid(row=0, column=0)

popup = Button(main, text="Press ME!!!!!!!", font=(80), command=button_pressed)
popup.grid(row=1, column=0)


main.mainloop()
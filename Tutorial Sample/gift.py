from tkinter import *

def change_colour():
    button.config(bg='gold')

def change_colour2():
    button2.config(bg='yellow')
    button.config(bg='gold')


main = Tk()

button = Button(main, text="Button", font=(80), bg='red', command=change_colour)
button.pack()
button2 = Button(main, text="Button 2", font=(80), bg='grey', command=change_colour2)
button2.pack()

main.mainloop()
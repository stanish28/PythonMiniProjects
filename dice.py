import random
from tkinter import *

root = Tk()
root.geometry("600x600")



def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

l1 = Label(root,font=("times", 200))

b1 = Button(root, text="Lets roll", command=roll)
b1.place (x=270, y=0)

root.mainloop()
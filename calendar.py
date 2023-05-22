from tkinter import *
from tkcalendar import *



root = Tk()
root.geometry("500x600")
root.title("CALENDAR")
root.config(background="#A1CDEC")

def selectDate():
    myDate = cal.get_date()
    selectedDate = Label(text= myDate)
    selectedDate.place(x=100,y=320)

cal = Calendar(root, setmode = 'day', date_pattern = 'dd/mm/yyyy',background="black",
                disabledbackground="black", bordercolor="black", 
               headersbackground="black", normalbackground="black", foreground='white', 
               normalforeground='black', headersforeground='black')
cal.config(background = "black")

cal.place(x=100,y=100)

submit = Button(root, text="Select Date", command=selectDate)

submit.place(x=100,y=350)


root.mainloop() 
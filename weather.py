import requests
from tkinter import *

def weather():
    city = enterCity.get()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=ddba93917c83c963e8bb1d8529d85a2a".format(city)

    res = requests.get(url)
    output = res.json()

    weather_data = output['weather'][0]['description']
    temperature_data = output['main']['temp']
   
    temperature_data = temperature_data-273.15
    weather_status.config(text="Weather status: " + str(weather_data))
    temperature_status.config(text="Temperature: " + str(round(temperature_data,2)) + " C")


window=Tk()
window.geometry("500x500")
window.config(background="white")

enterCity = Entry(window)
enterCity.grid(row=2,column=2,padx=150,pady=150)
enterCity.config(background="grey")

button1 = Button(window,text="Submit",command=weather,borderwidth=0,bg="white")
button1.grid(row=3,column=2,padx=50,pady=50)

weather_status = Label(window,font=("times", 10, "bold"))
weather_status.grid(row=4,column=2)


temperature_status = Label(window,font=("times", 10, "bold"))
temperature_status.grid(row=5,column=2)



window.mainloop()
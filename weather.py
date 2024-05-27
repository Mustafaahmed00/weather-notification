import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    try:
        # This is the complete url to get weather conditions of a city
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)  # requesting for the content of the url
        x = response.json()  # converting it into json 
        
        if x["cod"] != 200:
            raise Exception(x["message"])
        
        y = x["main"]  # getting the "main" key from the json object

        # getting the "temp" key of y
        temp = y["temp"]
        temp -= 273.15  # converting temperature from kelvin to celsius

        # storing the value of the "pressure" key of y
        pres = y["pressure"]

        # getting the value of the "humidity" key of y
        hum = y["humidity"]

        # storing the value of "weather" key in variable z
        z = x["weather"]

        # getting the corresponding "description"
        weather_desc = z[0]["description"]

        # combining the above values as a string 
        info = f"Here is the weather description of {cityName}:\nTemperature = {temp:.2f}°C\nAtmospheric pressure = {pres} hPa\nHumidity = {hum}%\nDescription of the weather = {weather_desc}"

        # showing the notification 
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=2
        )
        # waiting time
        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error', str(e))  # show pop up message if any error occurred

# creating the window
wn = Tk()
wn.title("PythonGeeks Weather Desktop Notifier")
wn.geometry('700x250')
wn.config(bg='#EAECEE')  # Set background color to a light grey

# Heading label
title_label = Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Helvetica', 18, 'bold'), fg='#1A5276', bg='#EAECEE')
title_label.pack(pady=20)

# Frame for input and button
frame = Frame(wn, bg='#EAECEE')
frame.pack(pady=10)

# Getting the place name 
Label(frame, text='Enter the Location:', font=("Helvetica", 13), bg='#EAECEE').grid(row=0, column=0, padx=10, pady=5)

place = StringVar(wn)
place_entry = Entry(frame, width=50, textvariable=place, font=("Helvetica", 12), bd=2, relief=SOLID)
place_entry.grid(row=0, column=1, padx=10, pady=5)

# Button to get notification
btn = Button(frame, text='Get Notification', font=("Helvetica", 10, 'bold'), fg='#FFFFFF', bg='#1A5276', activebackground='#5499C7', bd=2, relief=RAISED, command=getNotification, highlightthickness=2, highlightbackground='black')
btn.grid(row=1, columnspan=2, pady=20)

# Styling for the entry and button
place_entry.config(highlightbackground='black', highlightcolor='black')
btn.config(highlightbackground='black', highlightcolor='black')

# Run the window till closed by user
wn.mainloop()


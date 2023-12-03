import tkinter as tk
import requests


def getweather():
    city = cityentry.get()
    unit = unitsvar.get()
    apikey = '8579a6d068c1ef291b15446d86aec910'

    if city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units={unit}'
        response = requests.get(url)
        weatherdata = response.json()

        if response.status_code == 200:
            temperature = weatherdata['main']['temp']
            humidity = weatherdata['main']['humidity']
            windspeed = weatherdata['wind']['speed']

            if unit == 'Celsius':
                unitlabel = '°C'
            else:
                unitlabel = '°F'

            resultlabel.config(
                text=f'Temperature: {temperature} {unitlabel}\nHumidity: {humidity}%\nWind Speed: {windspeed} m/s')
        else:
            resultlabel.config(text='City not found')


app = tk.Tk()
app.geometry("250x270")
app.title('Weather App')
app.configure(bg='lightblue')
citylabel = tk.Label(app, text='Enter City:', font=('Arial', 12),bg='lightblue')
citylabel.pack(pady=10)

cityentry = tk.Entry(app, font=('Arial', 12))
cityentry.pack()

unitslabel = tk.Label(app, text='Select Units:', font=('Arial', 12),bg='lightblue')
unitslabel.pack(pady=10)

unitsvar = tk.StringVar(app)
unitsvar.set('Celsius')
unitsoption = tk.OptionMenu(app, unitsvar, 'Celsius', 'Fahrenheit')
unitsoption.pack(pady=5)

showweatherbutton = tk.Button(app, text='Show Weather', command=getweather, font=('Arial', 12))
showweatherbutton.pack(pady=10)

resultlabel = tk.Label(app, font=('Arial', 12), wraplength=300,bg='lightblue')
resultlabel.pack()

app.mainloop()

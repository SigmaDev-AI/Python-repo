# create Really cool python program
import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '6b76b685de93272c00c902906129a4eb'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.city_label = tk.Label(root, text="Enter city name:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_info = tk.Label(root, text="", font=("Helvetica", 16))
        self.weather_info.pack()

    def get_weather(self):
        city_name = self.city_entry.get()
        if not city_name:
            messagebox.showerror("Error", "Please enter a city name")
            return

        complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            description = weather['description']

            weather_info = (
                f"Temperature: {temperature}°C\n"
                f"Pressure: {pressure} hPa\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description.capitalize()}"
            )
            self.weather_info.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()



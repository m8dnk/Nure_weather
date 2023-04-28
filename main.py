import tkinter as tk
import requests

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.label = tk.Label(master, text="Enter city name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Search", command=self.get_weather)
        self.button.pack()

        self.result = tk.Label(master, text="")
        self.result.pack()

    def get_weather(self):
        city = self.entry.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=6a30f6dcd86ad8343e6bd4d632c2688b"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            message = f"The temperature in {city} is {temp}°C, and the weather is {description}"
        else:
            message = "Sorry, we could not get the weather for that city."

        self.result.config(text=message)

root = tk.Tk()
window = MainWindow(root)
root.mainloop()

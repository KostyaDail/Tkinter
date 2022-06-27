# Погода в мире
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = "1a36f2053f841232b05f7594eb6aafbc"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


# funks
def print_weather(weather):
    try:
        city = weather["name"]
        country = weather["sys"]["country"]
        temp = weather["main"]["temp"]
        press = weather["main"]["pressure"]
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]
        desc = weather["weather"][0]["description"]
        sunrise_ts = weather["sys"]["sunrise"]
        sunset_ts = weather["sys"]["sunset"]
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime("%H:%M:%S", sunrise_struct_time)
        sunset = time.strftime("%H:%M:%S", sunset_struct_time)
        return f"Местоположение: {city}, {country} \nТемпература: {temp} °C " \
               f" °C \nАтм. давление: {press} гПа " \
               f"\nВлажность: {humidity}% \nСкорость ветра: {wind} м/с \nПогодные условия: {desc} " \
               f"\nВосход: {sunrise} \nЗакат: {sunset}"
    except:
        return "Ошибка получения данных..."


def get_weather(event=""):
    if not entry.get():
        messagebox.showwarning("Warning", "Ведите запрос в формате city, Country_Code")
    else:
        params = {
            "appid": API_KEY,
            "q": entry.get(),
            "units": "metric",
            "lang": "ru"
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label["text"] = print_weather(weather)


def about_program():
    messagebox.showinfo(title="О программе", message="Погода в мире")


def request_example():
    messagebox.showinfo(title="Пример запроса", message="Moscow, RU (Москва)")


root = ThemedTk(theme="arc")
root.title("Weather")
root.geometry("500x400+700+300")
root.iconbitmap("C:\\Users\\Kaide\\Desktop\\PythonProject\\pythonHub\\TKINTER\\Weather\\weather.ico")
root.resizable(False, False)
root.configure(background="#4682B4")

# Menu
main_menu = Menu(root)
root.config(menu=main_menu)
menu = Menu(main_menu, tearoff=0)

menu.add_command(label="Пример запроса", command=request_example)
menu.add_separator()
menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=menu)

# Стили
s = ttk.Style()
s.configure("TLabel", padding=10, font="Arial 12", background="#F0F8FF")
s.configure("TButton", font="Arial 11")
s.configure("TEntry", padding=5)

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="n")

entry = ttk.Entry(top_frame, font="Arial 11")
entry.place(relwidth=0.8, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor="n")

label = ttk.Label(lower_frame, anchor="nw")
label.place(relwidth=1, relheight=1)

# Назначение клавиши Enter
entry.bind("<Return>", get_weather)

root.mainloop()

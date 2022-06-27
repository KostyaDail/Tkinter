# Конвертер валют

from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root = Tk()
root.geometry("350x350+800+300")
root.title("Конвертор валют")
root.iconbitmap("change.ico")
root.resizable(False, False)

# Starting amount
START_AMOUNT = 1000


# Functions
def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    e_gbp.delete(0, END)
    e_cny.delete(0, END)
    try:
        e_usd.insert(0, round(float(e_rur.get()) / float(JSON_object["Valute"]["USD"]['Previous']), 2))
        e_eur.insert(0, round(float(e_rur.get()) / float(JSON_object["Valute"]["EUR"]['Previous']), 2))
        e_gbp.insert(0, round(float(e_rur.get()) / float(JSON_object["Valute"]["GBP"]['Previous']), 2))
        e_cny.insert(0, round(float(e_rur.get()) / float(
            JSON_object["Valute"]["CNY"]['Previous'] / JSON_object["Valute"]["CNY"]["Nominal"]), 2))
    except:
        messagebox.showwarning('Warning', 'Проверьте введенную сумму')


try:
    html = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror("Error", 'Ошибка получения курсов валют')

# Header Frame
header_frame = ttk.Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Header
h_currency = Label(header_frame, text="Валюта", bg="#ccc", font="Arial 14 bold")
h_currency.grid(row=0, column=0, sticky=EW)
h_buy = Label(header_frame, text="Покупка", bg="#ccc", font="Arial 14 bold")
h_buy.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Arial 14 bold")
h_sale.grid(row=0, column=2, sticky=EW)

# USD course
usd_currency = Label(header_frame, text="USD", font="Arial 12")
usd_currency.grid(row=1, column=0, sticky=EW)
usd_buy = Label(header_frame, text=JSON_object["Valute"]["USD"]['Previous'], font="Arial 12")
usd_buy.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text=JSON_object["Valute"]["USD"]['Value'], font="Arial 12")
usd_sale.grid(row=1, column=2, sticky=EW)

# EUR course
eur_currency = Label(header_frame, text="EUR", bg="#ccc", font="Arial 12")
eur_currency.grid(row=2, column=0, sticky=EW)
eur_buy = Label(header_frame, text=JSON_object["Valute"]["EUR"]['Previous'], bg="#ccc", font="Arial 12")
eur_buy.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text=JSON_object["Valute"]["EUR"]['Value'], bg="#ccc", font="Arial 12")
eur_sale.grid(row=2, column=2, sticky=EW)

# GBP course
gbp_currency = Label(header_frame, text="GBP", font="Arial 12")
gbp_currency.grid(row=3, column=0, sticky=EW)
gbp_buy = Label(header_frame, text=JSON_object["Valute"]["GBP"]['Previous'], font="Arial 12")
gbp_buy.grid(row=3, column=1, sticky=EW)
gbp_sale = Label(header_frame, text=JSON_object["Valute"]["GBP"]['Value'], font="Arial 12")
gbp_sale.grid(row=3, column=2, sticky=EW)

# CNY course
cny_currency = Label(header_frame, text="CNY", bg="#ccc", font="Arial 12")
cny_currency.grid(row=4, column=0, sticky=EW)
cny_buy = Label(header_frame, text=JSON_object["Valute"]["CNY"]['Previous'] / JSON_object["Valute"]["CNY"]["Nominal"],
                bg="#ccc", font="Arial 12")
cny_buy.grid(row=4, column=1, sticky=EW)
cny_sale = Label(header_frame, text=JSON_object["Valute"]["CNY"]['Value'] / JSON_object["Valute"]["CNY"]["Nominal"],
                 bg="#ccc", font="Arial 12")
cny_sale.grid(row=4, column=2, sticky=EW)

# Calc Frame
calc_frame = Frame(root, bg="#fff")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# RUR
l_rur = Label(calc_frame, text="Рубль:", bg="#fff", font="Arial 12 bold")
l_rur.grid(row=0, column=0, padx=10)
e_rur = ttk.Entry(calc_frame, justify=CENTER, font="Arial 12")
e_rur.grid(row=0, column=1, columnspan=2, pady=15, padx=10, sticky=EW)
e_rur.insert(0, START_AMOUNT)

s = ttk.Style()
s.theme_use("alt")
s.configure("TButton", background="#343D46", foreground="orange", font=("Helvetica", 14, "bold"))

# Button
btn_calc = ttk.Button(calc_frame, text="Обмен", command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

# Result Frame
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=15)
res_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(res_frame, text="USD:", font="Arial 12 bold")
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font="Arial 12")
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, round(START_AMOUNT / float(JSON_object["Valute"]["USD"]['Previous']), 2))

# EUR
l_eur = Label(res_frame, text="EUR:", font="Arial 12 bold")
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font="Arial 12")
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, round(START_AMOUNT / float(JSON_object["Valute"]["EUR"]['Previous']), 2))

# GBP
l_gbp = Label(res_frame, text="GBP:", font="Arial 12 bold")
l_gbp.grid(row=4, column=0)
e_gbp = ttk.Entry(res_frame, justify=CENTER, font="Arial 12")
e_gbp.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)
e_gbp.insert(0, round(START_AMOUNT / float(JSON_object["Valute"]["GBP"]['Previous']), 2))

# CNY
l_cny = Label(res_frame, text="CNY:", font="Arial 12 bold")
l_cny.grid(row=5, column=0)
e_cny = ttk.Entry(res_frame, justify=CENTER, font="Arial 12")
e_cny.grid(row=5, column=1, columnspan=2, padx=10, sticky=EW)
e_cny.insert(0, round(
    START_AMOUNT / float(JSON_object["Valute"]["CNY"]['Previous'] / JSON_object["Valute"]["CNY"]["Nominal"]), 2))

root.mainloop()

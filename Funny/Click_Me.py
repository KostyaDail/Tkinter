from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Веселая Кнопка")
root.geometry("500x150+600+300")
root.iconbitmap("But.ico")
root.config(bg="#B0C4DE")
root.resizable(False, False)


def open_win():
    win = Toplevel()
    win.resizable(False, False)
    win.image = PhotoImage(file="picture.png")
    bg_logo = Label(win, image=win.image)
    bg_logo.grid(row=0, column=0)
    """ 
    Метод overrideredirect - указание оконному менеджеру игнорировать это окно. Если аргумент
    равен True, то такое окно будет показано оконным менеджером без обрамления.
    Может быть использован, например, для создания splashscreen при старте программы.
    """
    win.overrideredirect(True)
    # Устанавливает фокус на окно win, даже при наличии открытых других окон
    win.grab_set()


# объект класса Style()
s = ttk.Style()
s.theme_use("alt")
s.configure(".", background="#343D46", foreground="orange", font=("Helvetica", 25, "bold"))
# Кнопка
btn_start = ttk.Button(root, text="Нажми меня =)", command=open_win)
btn_start.place(relx=0.5, rely=0.5, width=300, anchor=CENTER)

root.mainloop()

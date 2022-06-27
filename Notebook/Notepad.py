# Программа блокнот

# импортируем модуль tkinter
from tkinter import *
# импортируем модуль диалоговых окон отдельно
from tkinter import messagebox
from tkinter import filedialog

# Экземпляр класса TK и его настройка
root = Tk()
root.geometry("1000x600+500+200")
root.title("Блокнот")
root.iconbitmap("Notepad.ico")

# Экземпляр класса Menu
main_menu = Menu(root)
root.config(menu=main_menu)


# функция окно о программе
def about_program():
    messagebox.showinfo(title="О редакторе", message="Простейший блокнот")


# функция закрыть программу
def pad_quit():
    answer = messagebox.askyesno(title="Выход", message="Закрыть программу?")
    if answer:
        root.destroy()


# функция открыть файл
def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла", filetypes=(("Текстовые документы (*.txt)", "*.txt"),
                                                                           ("Все файлы", "*.*")))
    if file_path:
        t.delete("1.0", END)
        f = open(file_path, "rt", encoding="utf_8")
        t.insert("1.0", f.read())
        f.close()


# функция сохранить файл
def save_file():
    file_path = filedialog.asksaveasfilename(title="Сохранение файла",
                                             filetypes=(("Текстовые документы (*.txt)", "*.txt"),
                                                        ("Все файлы", "*.*")))
    f = open(file_path, "w", encoding="utf-8")
    text = t.get("1.0", END)
    f.write(text)
    f.close()


# функция очистить экран
def clear_text():
    t.delete("1.0", END)


# функция для изменения тем редактора
def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


# Каскадное меню Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
# создадим разделитель между пунктами меню
file_menu.add_separator()
file_menu.add_command(label="Очистить экран", command=clear_text)
# еще разделитель между пунктами меню
file_menu.add_separator()
file_menu.add_command(label="Выход", command=pad_quit)
main_menu.add_cascade(label="Файл", menu=file_menu)

# Меню тем. Выпадающее меню.
theme_menu = Menu(main_menu, tearoff=0)

theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light Theme", command=lambda: change_theme("light"))
theme_menu_sub.add_command(label="Dark Theme", command=lambda: change_theme("dark"))

theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=theme_menu)

# Виджет Frame. Заполняем им весь экран.
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# словарь с цветовыми параметрами тем
theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#fff", "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000FF", "select_bg": "#777"
    }
}
# Виджет Text.
t = Text(f_text, bg=theme_colors["dark"]["text_bg"], fg=theme_colors["dark"]["text_fg"], padx=10, pady=10, wrap=WORD,
         width=30, font=("Courier New", 12), insertbackground=theme_colors["dark"]["cursor"],
         selectbackground=theme_colors["dark"]["select_bg"], spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

# Scrollbar
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)


# Горячие клавиши
def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


root.bind_all("<Key>", _onKeyRelease, "+")

root.mainloop()

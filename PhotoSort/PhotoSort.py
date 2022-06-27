# Программа PhotoSort
"""
Сортировщик Фотографий (файлов).
Пользователь выбирает папку с файлами. Программа считывает эти файлы и создает список.
Программа проходит по этому списку, берет дату изменения каждого файла, создает папку 
с датой этого файла и перемещает файл в эту папку. Если папка такая уже существует, 
то файл перемещается внутрь ее. По завершению работы программы
все файлы должны быть отсортированы по папкам с датой их создания.
"""

# Импортируем модули, которые нам понадобятся.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime


def choose_dir():
    """Выбирает папку с файлами для сортировки и подставляет его в поле e_path"""
    # выбор папки (пути) с помощью диалогового окна
    dir_path = filedialog.askdirectory()
    # удаляем старый путь
    e_path.delete(0, END)
    # подставляем новый путь в поле
    e_path.insert(0, dir_path)


def f_start():
    """Получает путь папки, который выбрал пользователь, и запускает процесс сортировки в ней файлов"""
    # получаем путь из поля e_path
    cur_path = e_path.get()
    if cur_path:
        # берем каждую папку, подпапку, файлы и пройдемся по этой структуре (os.walk(cur_path))
        for folder, subfolders, files in os.walk(cur_path):
            # Для каждого файлы из списка в структуре os.walk(cur_path)
            for file in files:
                # получим полный путь к файлу
                path = os.path.join(folder, file)
                # получим время модификации файла
                m_time = os.path.getmtime(path)
                # преобразование даты к нужному формату
                date = datetime.fromtimestamp(m_time)
                date = date.strftime("%d-%m-%Y")  # DD-MM-YYYY
                # Создадим новый путь, который состоит из пути текущей папки и даты файла
                date_folder = os.path.join(cur_path, date)
                # Если не существует такой папки (пути date_folder), то создадим папку
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                # перемещаем файл (file) в эту папку (date_folder)
                os.rename(path, os.path.join(date_folder, file))
        # Сообщение об успехе
        messagebox.showinfo("Success", "Сортировка выполнена успешно")
        # удаляем путь из поля e_path
        e_path.delete(0, END)
    else:
        # Сообщение о неудачи
        messagebox.showwarning("Warning", "Выберите папку с фотографиями (файлами)")


doc_str = """Сортировщик Фотографий (файлов).
По завершению работы программы, все файлы будут отсортированы по папкам с датой их создания."""


def about_program():
    messagebox.showinfo(title="О программе", message=doc_str)


root = Tk()
root.title("PhotoSort")
root.geometry("600x160+600+300")
root.iconbitmap("ico_1.ico")
root.config(bg="#B0C4DE")
root.resizable(True, False)

# Меню программы
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_cascade(label="О программе", command=about_program)

# Создадим Frame, где мы будем размещать кнопку выбора папки и поле (Entry),
# где будет показан путь после выбора папки
frame = Frame(root, bg="#4682B4", bd=5)
frame.pack(pady=10, padx=10, fill=X)

# Разметим на frame элементы
# Создадим поле отображения пути.
e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=5, expand=True, fill=X)

# Создадим кнопку выбора папки, и разместим ее тоже на frame
btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=10, ipady=4)

# Создадим кнопку старта программы, и разместим ее в окне root
btn_start = Button(root, text="Start", font=("Helvetica", 14, "bold"), command=f_start, bg="#343D46", fg="orange")
btn_start.pack(fill=X, padx=10, pady=15)

root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

# Создание приложения
app = tk.Tk()
app.title("Поисковая система")
app.configure(background="#ececec")

# Надпись
search_label = ttk.Label(app, text="Поиск", font="verdana 18 underline", foreground="#333")
search_label.grid(row=0, column=1)

# Текстовое поле
text_field = ttk.Entry(app, width=40)
text_field.grid(row=1, column=1)

# Сразу выбран Яндекс
search_engine = StringVar()
search_engine.set("yandex")

def search():
  if text_field.get().strip() !="":
    if search_engine.get() == "google":
      webbrowser.open ('https://www.google.ru/search?q=' + text_field.get ())
    elif search_engine.get() == "yandex":
      webbrowser.open ('https://yandex.ru/search/?lr=75&text=' + text_field.get ())
  else:
    pass

def searchBtn():
  search()

def enterBtn(event):
  search()

# Кнопка поиска
btn_search = ttk.Button(app, text="Найти", width=10, command=searchBtn)
btn_search.grid(row=1, column=2)

text_field.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text="Google", value="google", variable=search_engine)
radio_google.grid(row=2, column=1, sticky=W)

radio_yandex = ttk.Radiobutton(app, text="Yandex", value="yandex", variable=search_engine)
radio_yandex.grid(row=2, column=1, sticky=E)

app.wm_attributes('-topmost', True)

text_field.focus()
# Вечный цикл
app.mainloop()
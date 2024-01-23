import matplotlib.pyplot as plt
import numpy as np
import keyboard
from tkinter import *
from tkinter import messagebox

def get_data_in_func_with_degree_mode():
    global degree
    data = entry_degree.get()
    degree = data
    fig, ax = plt.subplots()
    xmin, xmax = -5, 5
    ymin, ymax = -5, 5
    plt.plot([xmin, xmax], [0, 0], '-')
    plt.grid(linestyle='-', color='black')
    plt.axis([xmin, xmax, ymin, ymax])         
    x = np.linspace(-5, 5, 100)
    y = x**int(degree)
    ax.plot(x, y)
    plt.show()

def back_to_main_menu_from_degree_func_mode():
    try:
      entry_degree.destroy()
      label_degree.destroy()  
      button_calc_degree.destroy() 
      button_back_to_select.destroy()
    except NameError:
        messagebox.showerror(title="Ошибка", message="Ошибка, обратитесь к разработчику для решения данной проблемы")
    create_intro()

def back_to_main_menu_from_kxb_line_func_mode():
    try:
      result_button.destroy()
      label_linear.destroy()
      button_back_to_select.destroy()
      entry_k.destroy()
      create_intro()
    except NameError:
        messagebox.showerror(title="Ошибка. Обратитесь к разработчику для решения данной проблемы.")


def kxb_line_func():
    global result_button
    global label_linear
    global entry_k
    global entry_b
    global button_back_to_select
    destroy_intro()
    label_linear = Label(root, text="y =    x +")
    label_linear.place(x=10, y=45)
    entry_k = Entry(root, width=int(0.5))
    entry_k.place(x=31, y=45)
    button_back_to_select = Button(root, text="<- Назад в главное меню", command=back_to_main_menu_from_kxb_line_func_mode)
    button_back_to_select.place(x=10, y=10)
    entry_b = Entry(root, width=int(0.5))
    entry_b.place(x=60, y=45)
    result_button = Button(root, text="Результат", command=get_data_in_kxb_line_func_mode)
    result_button.place(x=80, y=45)
    keyboard.on_press_key(key="enter", callback=get_data_in_kxb_line_func_mode)

def get_data_in_kxb_line_func_mode():
    try:
      k = int(entry_k.get())
      b = int(entry_b.get())
    except ValueError:
        messagebox.showerror(title="Ошибка", message="Ошибка. Задано недопустимое число.")  
    fig, ax = plt.subplots()
    xmin, xmax = -5, 5
    ymin, ymax = -5, 5
    plt.plot([xmin, xmax], [0, 0], '-')
    plt.grid(linestyle='-', color='black')
    plt.axis([xmin, xmax, ymin, ymax])         
    x = np.linspace(-5, 5, 100)
    y = k*x+b
    ax.plot(x, y)
    plt.show()

   
   
def func_with_degree():
    global entry_degree
    global button_calc_degree
    global button_back_to_select
    global label_degree
    destroy_intro()
    label_degree = Label(root, text="y=x")
    label_degree.place(x=10, y=45)
    entry_degree = Entry(root, width=1)
    entry_degree.place(x=35, y=40)
    button_calc_degree = Button(root, text="Результат", command=get_data_in_func_with_degree_mode)
    button_calc_degree.place(x=55, y=45)
    button_back_to_select = Button(root, text="<- Назад в главное меню", command=back_to_main_menu_from_degree_func_mode)
    button_back_to_select.place(x=10, y=10)
    keyboard.on_press_key(key="enter", callback=get_data_in_func_with_degree_mode)


def destroy_intro():
    label_intro.destroy()
    button_select_degree.destroy()
    button_select_linear.destroy()

def create_intro():
    global label_intro
    global button_select_degree
    global button_select_linear
    label_intro = Label(font="Arial 10", text="Здравствуйте! Перед началом работы выберите режим.")
    label_intro.place(x=10, y=10)
    button_select_degree = Button(root, text="Функция со степенью", command=func_with_degree)
    button_select_degree.place(x=10, y=40)
    button_select_linear = Button(root, text="Линейная функция y = kx + b", command=kxb_line_func)
    button_select_linear.place(x=10, y=80)

root = Tk()
root.title("Графопостроитель")
root.geometry("500x500")

create_intro()
root.mainloop()
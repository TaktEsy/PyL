import tkinter as tk

def get_values():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    return num1, num2
2
def insert_values(val):
    answer.delete(0, "end")
    answer.insert(0, val)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


# Окно программы
window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(width=False, height=False)

# Кнопки
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=100, y=200)

button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)

button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)

button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)

# Поля ввода/вывода
num1_entry = tk.Entry(window, width=28)
num1_entry.place(x=100, y=75)

num2_entry = tk.Entry(window, width=28)
num2_entry.place(x=100, y=150)

answer = tk.Entry(window, width=28)
answer.place(x=100, y=300)

# Надписи
lab1 = tk.Label(window, text="Число 1:")
lab1.place(x=100, y=50)

lab2 = tk.Label(window, text="Число 2:")
lab2.place(x=100, y=125)

lab3 = tk.Label(window, text="Ответ:")
lab3.place(x=100, y=275)

window.mainloop()

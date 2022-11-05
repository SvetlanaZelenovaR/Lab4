import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Generator import generator
import time
import pygame


def key_generation():
    field_key.configure(text=generator(), font=('Comic Sans MS', 10))


def close():
    global run
    choice = messagebox.askyesno('Выход', 'Вы хотите выйти?')
    if choice:
        window.destroy()
        run = False


# Добавление музыки
pygame.mixer.init()
pygame.mixer.music.load('turtle_music.mp3')
pygame.mixer.music.play(-1)

window = tk.Tk()
window.title("Turtle Odyssey 2")
window.geometry('800x600')

# Добавление изображения на фон
Im = tk.PhotoImage(file='turtleO.png')
label_Im = tk.Label(window, image=Im)
label_Im.place(relx=0, rely=0)

frame = tk.Frame(window, background='#ADD8E6')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Создание холста для анимации
canvas = Canvas(window, width=300, height=100, highlightthickness=0, bg='#4682B4')
canvas.grid(column=0, row=0)

# Добавление объекта анимации
obj = PhotoImage(file='Nevosoft_logo.png')
obj_move = canvas.create_image(300, 100, anchor='se', image=obj)

lbl_Intro1 = tk.Label(frame, text='У вас осталось 30 минут игры!', font=('Comic Sans MS', 20), bg='#ADD8E6')
lbl_Intro1.grid(column=1, row=0, padx=10, pady=20)

lbl_Intro2 = tk.Label(frame, text='Чтобы снять ограничение, введите ключ', font=('Comic Sans MS', 20), bg='#ADD8E6')
lbl_Intro2.grid(column=1, row=1, padx=10, pady=20)

field_key = tk.Label(frame, width=30)
field_key.grid(column=1, row=2, padx=10, pady=20)

enter_key = tk.Button(frame, text='Generate a key', font=("Comic Sans MS", 15), command=key_generation, bg='#4682B4')
enter_key.grid(column=0, row=3)

exxit = tk.Button(frame, text='Cancel', font=("Comic Sans MS", 15), command=close, bg='#4682B4')
exxit.grid(column=2, row=3)

# Добавление анимации
run = True
while run:
    canvas.move(obj_move, 30, 0)
    canvas.update()
    time.sleep(1)
    canvas.move(obj_move, -30, 0)
    canvas.update()
    time.sleep(1)

window.mainloop()

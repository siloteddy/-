import tkinter as tk
import random
from settings import *

def click():
    global score
    button.configure(text = 'take a card')
    while True:
        random_key = random.choice(list(cards.keys()))
        texts.append(random_key)
        score += (cards[random_key])
        break
    print(texts)
    label_spis.configure(text = texts)
    label_score.configure(text = score)
    
def deleted():
    global score
    texts.clear()
    label_spis.configure(text = 'you do not have any cards')
    score = 0
    label_score.configure(text = 0)

win = tk.Tk()

win.geometry(f"{W}x{H}")
win.resizable(0,0)

cards = {'ace': 11,
               'ten': 10,
               'king': 4,
               'lady': 3,
               'jack': 2,
               'nine': 9,
               'eight': 8,
               'seven': 7,
               'six': 6,
               }

score = 0

texts = []

button = tk.Button(bg = COLOR_1, fg = COLOR_2,font = ('Franklin Gothic',12), text = "Взять Карту/ Начать игру", command=lambda: click())
button.place(x = 70, y = 60, width = 230, height = 80)

button_2 = tk.Button(bg = COLOR_1, fg = COLOR_2,font = ('Franklin Gothic',12),text = 'Сбросить руку',command=lambda: deleted())
button_2.place(x = 70,y = 160, width = 230, height = 80)


label = tk.Label(text='list cards:', fg = COLOR_1, font = ('Franklin Gothic',15))
label.place(x = 80,y = 250)

label_spis = tk.Label(text= texts, fg = COLOR_1, font = ('Franklin Gothic',10))
label_spis.place(x = 75,y = 275)

label_score_sum = tk.Label(text='total points:', fg = COLOR_1, font = ('Franklin Gothic',15))
label_score_sum.place(x = 80,y = 300)

label_score = tk.Label(text= score, fg = COLOR_1, font = ('Franklin Gothic',10))
label_score.place(x = 75,y = 327)

win.mainloop()
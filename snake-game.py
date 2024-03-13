from tkinter import *
import random


GAME_WIDTH = 600
GAME_HEIGHT = 600

SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00ff00'
FOOD_COLOR = '#ff0000'
BACKGROUND_COLOR = '#000'


class Snake:
    pass

class Food:
    pass

def check_collision():
    pass

def game_over():
    pass 


window = Tk()

window.title('snake game')
window.resizable(False, False)


score= 0
direction  = 'down'

label = Label(window, text= "Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width =  window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

window.geometry(f"{window_width} x {window_height} + {x} + {y}")


window.mainloop()
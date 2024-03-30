import turtle
import time
import random

WIDTH, HEIGHT = 600, 600
COLORS = ['red', 'green', 'Yellow', 'black', 'pink', 'cyan', 'blue', 'skyblue','purple', 'grey']

def init_screen():
    SCREEN = turtle.Screen()
    SCREEN.setup(WIDTH, HEIGHT)
    SCREEN.title("Turtle Racing! ")

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles1 = []
    spaceingX = WIDTH // (len(colors) +1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spaceingX, -HEIGHT//2 + 20)
        racer.pendown()
        turtles1.append(racer)
    
    return turtles1

def get_number_of_racer():
    racers = 0
    while True:
        racers = input("Enter the number of racer (2- 8) : ")
        if racers.isdigit():
            racers = int(racers)
            if 1< racers <=10:
                break
            else: 
                print(f"please enter between 2 -8")
        else:
            print(f'Please enter in number : ')
    return racers

racers = get_number_of_racer()
init_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner)

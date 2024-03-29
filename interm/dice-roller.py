import random

# ● ┌ ─ ┐ │ └ ┘

"┌───────────┐"
"│           │"
"│     ●     │"
"│           │"
"└───────────┘"


dice_art = {
    1: ( "┌───────────┐", 
         "│           │", 
         "│     ●     │", 
         "│           │", 
         "└───────────┘" ),
    2: ( "┌───────────┐", 
         "│  ●        │", 
         "│           │", 
         "│        ●  │", 
         "└───────────┘" ),
    3: ( "┌───────────┐", 
         "│  ●        │", 
         "│     ●     │", 
         "│        ●  │", 
         "└───────────┘" ),
    4: ( "┌───────────┐", 
         "│  ●     ●  │", 
         "│           │", 
         "│  ●     ●  │", 
         "└───────────┘" ),
    5: ( "┌───────────┐", 
         "│  ●     ●  │", 
         "│     ●     │", 
         "│  ●     ●  │", 
         "└───────────┘" ),
    6: ( "┌───────────┐", 
         "│  ●     ●  │", 
         "│  ●     ●  │", 
         "│  ●     ●  │", 
         "└───────────┘" ),
}

def num_of_dice1():
    num = input("Enter number of dice : ")
    while True:
        if num.isdigit():
            num = int(num)
            break
        else:
            print(f" enter correct number in integer")
    return num

dice = []
total = 0
num_of_dice = num_of_dice1()

for _ in range(num_of_dice):
    dice.append(random.randint(1,6))


print(dice)


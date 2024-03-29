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

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die

print(f"total : {total}")
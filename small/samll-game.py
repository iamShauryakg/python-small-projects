import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()

while True:
    players = input("enter the no of player (1-4): ")
    
    if players.isdigit():
        players = int(players)
        if 1 < players and 4 >= players:
            break 
        else:
            print("players must be between 1 to 4 ")
            print("not valid input")
            continue
    else:
        print("Invalid, try again. ")
    

print(players)

max_score = 50

player_scores = [ 0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:
    for i in range(players):
        print(f"\nPlayers {i + 1} turn has started \n")
        print(f' Your Total score is {player_scores[i]}')

        current_score = 0
        
        while True:
            should_roll = input("would you like to roll (y) : ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
        
            if value == 1:
                print(f"you roll 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print(f"you rolled a : {value}")
                print(f"you score is  a : {current_score}")
            
        player_scores[i] += current_score
        print(f"your score is : {current_score}")
        
max_score = max(player_scores)
winningidx = player_scores.index(max_score)

print(f"Player {winningidx + 1} WON")
print(player_scores)

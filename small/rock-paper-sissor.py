import random

user_win = 0
computer_win = 0

list_of_option = ['rock', 'paper', 'sissor']

while True:
    user_input = input("type Rock/Paper/Sissor or q to quit: ").lower()

    if user_input == 'q':
        break
    if user_input not in list_of_option:
        continue

    rand_number = random.randint(0,2)

    computer_option = list_of_option[rand_number]

    print(f'Computer option : {computer_option}')


    if user_input == 'rock' :
        if computer_option =='sissor':
            print(' You win!! ')
            user_win += 1
        elif computer_option == 'rock':
            print('draw')
        else:
            print(f'You Lose...')
            computer_win +=1
    if user_input == 'sissor' :
        if computer_option =='paper':
            print(' You win!! ')
            user_win += 1
        elif computer_option == 'sissor':
            print('draw')
        else:
            print(f'You Lose...')
            computer_win += 1
    if user_input == 'paper' :
        if computer_option =='rock':
            print(' You win!! ')
            user_win += 1
        elif computer_option == 'paper':
            print('draw')
        else:
            print(f'You Lose...')
            computer_win += 1

print(f'total Number of wins : {user_win}')

print(f'Have a great day. ')
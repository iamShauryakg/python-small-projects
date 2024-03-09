print(f'Welcome to small quiz game ...')

ask_play = input('do you want to play quiz game ? ')

if ask_play.lower() != 'yes':
    quit()

print(f" Okay let's play")



score = 0

ans = str(input(f'what does CPU stands for : '))
if ans.lower() == 'central processing unit' :
    print(f"Correct!")
    score += 1
else: 
    print(f" Incorrect !!")

ans = str(input(f'what does ROM stands for : '))
if ans.lower() == 'read only memory' :
    print(f"Correct!")
    score += 1
else: 
    print(f" Incorrect !!")

ans = str(input(f'what does GPU stands for : '))
if ans.lower() == 'graphics processing unit' :
    print(f"Correct!")
    score += 1
else: 
    print(f" Incorrect !!")

ans = str(input(f'what does RAM stands for : '))
if ans.lower() == 'random access memory' :
    print(f"Correct!")
    score += 1
else: 
    print(f" Incorrect !!")


print(f" score : {score}")
import random


inpnum = input('Enter your number : ')

if inpnum.isdigit():
    inpnum = int(inpnum)
    if inpnum < 0 :
        print('type a number greater then 0 ')
        quit()
else:
    print('Please type a number ')
    quit()

num = random.randint(0, inpnum)

print(num)

guess_times = 0
while True:
    guess_times +=1
    user_num = input(' Guess the number')
    if user_num.isdigit():
        user_num = int(user_num)
qu
        if user_num > num :
            print('the number is smaller')
        elif user_num < num:
            print('the num is greater')
        else: 
            print(f" You WIN!! ")
            print(f' You got it right in {guess_times} number of times')
            break
    else:
        print(f'please type a number next time. ')
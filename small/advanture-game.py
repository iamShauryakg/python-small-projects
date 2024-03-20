#small advanture game 

def adventure_game():
    ans = input('You are on a road and stuck on 3fold road you have only two option go right or go left which way will you go left or right : ').lower()

    if ans == 'left':
        river()
    elif ans == 'right':
        print('you choose the right path')
        bridge()
    else: 
        print('please choose right answer : ')

def river():
    ans = input(f'You come to a river, will you can walk around it or swim accross? Type "walk" to walk and "swim" to swim accross : ').lower()

    if ans == 'walk':
        print('you walk for many kilmeters and ran out of food supplies now you are dead. GAME OVER')
        
    elif ans == 'swim':
        print('You swim and was eaten by an alligetor . GAME OVER')
    else: 
        print(f'not valid option')
        river()

def bridge():
    ans = input(f"you came accros the bridge, it's very old would you like to walk on bridge or go back, type 'back' to go back or walk to walk on bridge. : ")

    if ans == 'walk':
        print('you cross the bridge. ')
        stranger()
    elif ans == 'back':
        print(f"you went back and took left road ")
        river()

    else:
        print('choose valid option')
        bridge()

def stranger():
    ans = input(f"you met a stranger. do you want to talk to him (yes/no) : ").lower()

    if ans == 'yes':
        print('you talk to stranger and he helped you to go home You WIN!. ')
    elif ans == 'no':
        print("you ignored the strange and he got offended . ")
        river()
    else:
        print(f'invalid option choose again')
        stranger() 

def play_again():
    ans = input('would you like to play again. yes/no : ').lower()

    if ans == 'yes':
        adventure_game()
    else: 
        print('have a nice day')

def main():
    name = input('Enter your name : ')
    print(f'Wlecome {name}, to this small advanture game ')
    
    
    play = input('do you want to play the game? yes or no ').lower()
    
    if play =='yes':
        adventure_game()
    else:
        print('see you next time  ')
    
    

main()
import turtle

def get_number_of_racer():
    racers = 0
    while True:
        racers = input("Enter the number of racer (2- 10) : ")
        if racers.isdigit():
            racers = int(racers)
            if 1< racers <=10:
                break
            else: 
                print(f"please enter between 2 -10")
        else:
            print(f'Please enter in number : ')
    return racers

racers = get_number_of_racer()
print(racers)
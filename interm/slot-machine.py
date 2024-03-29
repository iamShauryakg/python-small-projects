import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break 
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input(f"What woud you like to deposit ? rs ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amout must be greater then zero 0")
        else:
            print(f"Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on1 1 to {MAX_LINES} ? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES :
                break
            else:
                print(f"enter line between 1- {MAX_LINES}")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:
        amount = input(f"What woud you like to bet ({MIN_BET} - {MAX_BET}) ? rs ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(F"BET amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print(f"Please enter a number.")
    
    return amount

def spin1(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f" you do not have enough balance. Your current balance is {balance}rs . ")
        else:
            break
        
    print(f" You are betting {bet}rs on {lines} Lines. Total bet is : {total_bet} rs")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}. ")
    print(f"You won On lines : ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f" Current balance is {balance} rs")
        spin = input(" Press Enter to play (q to quit)")
        if spin == "q":
            break
        balance += spin1(balance)
    
    print(f" you left with {balance}")

main()
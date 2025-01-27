import random

MAX_LINES = 3
MAX_BET = 100000
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
    "B": 6,
    "C": 8,
    "D": 10
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Use `line + 1` to indicate the winning line
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        row_symbols = [column[row] for column in columns]
        print(" | ".join(row_symbols))  # Use " | " to join symbols in the row

def desposit():
    while True:
        amount = input("You Got the Money? Rs ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Dalle Paise Daal")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Sahi se Lines Choose Kar")
        else:
            print("Enter the Number of Lines you want to Bet")
    return lines

def get_bet():
    while True:
        bet = input("Enter the Amount You want to Bet? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter an amount Between Rs {MIN_BET} - Rs {MAX_BET}")
        else:
            print(" Enter the Correct Bet Amount")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Jaeb mai nhi hai Chabni or Juha Khelna hai? Current Balance is Rs {balance}. Add Money.")
        else:
            break

    print(f"You are Betting Rs {bet} on {lines} lines. Total bet is equal to: Rs {total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"Wow, You win this much fake digital money which has no value at all: Rs {winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = desposit()
    while True:
        print(f"Current balance is Rs {balance}")
        user_input = input("Press enter to play (q to quit): ")
        if user_input == "q":
            break
        balance += spin(balance)
    print(f"You left with Rs {balance}")

main()

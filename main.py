import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}   


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
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid amount. Please enter a valid number.")

    return amount


def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if lines>=1 and lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Invalid number. Please enter a valid number")

    return lines


def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Invalid amount. Please enter a valid number.")

    return amount


def main():
    while True:
        balance = deposit()
        lines = get_no_of_lines()
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is ${total_bet}")
    

main()
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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
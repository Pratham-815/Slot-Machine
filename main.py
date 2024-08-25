MAX_LINES = 3


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


def main():
    balance = deposit()
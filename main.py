
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid amount. Please enter a valid number.")

    return amount


deposit()
import random
from decouple import config


def casino():
    my_money = config('MY_MONEY', cast=int)
    balance = my_money
    while True:
        my_number = input("Choose any number between 1 and 30: ")
        try:
            my_number = int(my_number)
            if my_number not in range(1, 31):
                print("You entered the number which is not suitable!")
                continue
        except ValueError:
            print("Please enter only integers")
            continue

        my_bid = input("Choose your bid: ")
        try:
            my_bid = int(my_bid)
            if my_bid > balance:
                print(f'Your bid greater than your available balance: {balance}!')
                continue
        except ValueError:
            print("Please enter only integers")
            continue

        slot = random.randint(1, 31)
        if slot == my_number:
            my_cash = my_bid * 2
            balance += my_cash
        else:
            balance -= my_bid
        play_again = input("Do you want to continue? y/n: ")
        if play_again.lower() == 'y':
            continue
        if play_again.lower() == 'n':
            print(f'Four balance: {balance}')
            break

if __name__ == "__main__":
    casino()

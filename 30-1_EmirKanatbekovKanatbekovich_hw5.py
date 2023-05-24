import random
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
MY_MONEY = int(config['DEFAULT']['MY_MONEY'])

def play_game():
    capital = MY_MONEY
    slots = list(range(1, 31))

    while capital > 0:
        print(f"Ваш текущий капитал: ${capital}")
        bet = input("Введите ставку: $")
        chosen_slot = int(input("Выберите номер слота (1-30): "))

        if chosen_slot not in slots:
            print("Некорректный номер слота!")
            continue

        if int(bet) > capital:
            print("Недостаточно средств для ставки!")
            continue

        winning_slot = random.choice(slots)

        if chosen_slot == winning_slot:
            win_amount = int(bet) * 2
            capital += win_amount
            print(f"Вы выиграли! Выигрыш: ${win_amount}")
        else:
            capital -= int(bet)
            print("Вы проиграли!")

        play_again = input("Хотите сыграть еще? (да/нет): ")
        if play_again.lower() != "да":
            break

    print(f"Игра окончена. Ваш итоговый капитал: ${capital}")
    if capital > MY_MONEY:
        print("Вы в выигрыше!")
    elif capital == MY_MONEY:
        print("Вы остались при своих.")
    else:
        print("Вы в проигрыше.")

if __name__ == "__main__":
    play_game()


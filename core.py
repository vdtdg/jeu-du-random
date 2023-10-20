import random


def is_right_price(number: int, price: int):
    if number == price:
        print("You win ! You have guessed the right number.")
        return True
    elif number > price:
        print(f"Wrong, the price is less than {number}")
        return False
    else:
        print(f"Wrong, the price is more than {number}")
        return False


def game_round(range_min: int, range_max: int, max_attempts: int):
    print('-----------------')
    attempts = 1
    price = random.randint(range_min, range_max)  # Generate a random integer between the specified range
    print(f"You have {max_attempts} attempts to try to guess the a number between {range_min} and {range_max}.")
    while True:
        try:
            number = int(input(f"({attempts}/{max_attempts}) Please input a number and press enter: "))
        except Exception as e:
            print("Wrong input. Are you sure you typed a number ?")
            continue

        if is_right_price(number, price):
            break

        attempts += 1
        if attempts > max_attempts:
            print("You lose: maximum number of attempts exceeded.")
            break
    print('-----------------')


def run_game(round_configuration: dict):
    player_want_to_play = True
    while player_want_to_play:
        game_round(**round_configuration)
        replay = input('Want to play another round ? Input "r" and then enter. Else, just press enter.')
        if replay != "r":
            player_want_to_play = False

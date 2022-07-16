import random
import time


def print_pause(message_to_print, interval):
    print(message_to_print)
    time.sleep(interval)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.", 2)
    return response


def intro():
    print_pause("Only the strongest souls survive, will you become hollow?", 2)
    print_pause("You have to pick between a axe or sword.", 2)
    print_pause("May the fire in you heart guide you!", 2)
    print_pause("Stay on alert and don't let your guard down.", 2)


def get_weapon():
    response = valid_input("Please pick your weapon. "
                           "What will you pick? \n",
                           "axe", "sword")

    if "axe" in response:
        print_pause("Let this Axe make many Hollow!", 5)
    elif "sword" in response:
        print_pause("Let the blood run!", 5)
    print_pause("On to the quest.", 2)
    return response


def pick_path(weapon):
    response = valid_input("Would you like to open door to the witches house? "
                           "Choose 'yes' or 'no'.\n",
                           "yes", "no")
    adversary = pick_adversary()
    did_we_win = win_or_lose_fight()

    if "no" in response:
        print_pause("To the bonfire!", 2)
        print_pause("A boulder fell from the sky and CRUSHED YOU!", 8)
        print_pause("Game Over...", 1)
        play_again()

    elif "yes" in response:
        print_pause("Watch your back.", 2)
        print_pause("Woah! A " + adversary + " just attacked you!", 4)
        print_pause("You are now fighting the " + adversary + " with your " + weapon, 4)
        if did_we_win:
            print_pause("Victory!!!, you beat the " + adversary + " and they are now dead!", 2)
            print_pause("You kicked that things ass!", 1)
            print_pause("Congratulations, you won the game!", 2)
            play_again()
        else:
            print_pause("Oops...you got your ass kicked!", 5)
            play_again()


def play_again():
    new_game_response = valid_input("Would you like to play again? "
                                    "Choose 'yes' or 'no'. \n",
                                    "yes", "no")
    if "yes" in new_game_response:
        start_game()


def pick_adversary():
    adversaries = [
        "Witch",
        "Monster",
        "Demon"
    ]
    random_num = random.randint(0, len(adversaries) - 1)

    return adversaries[random_num]


def win_or_lose_fight():
    return random.choice([True, False])


def start_game():
    intro()
    weapon = get_weapon()
    pick_path(weapon)


start_game()

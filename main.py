import random
import sys

# generate a num between 1 and 5
def gen_num_of_items():
    return random.randint(1, 5)

def main():
    menu = True
    while menu:
        user_input = input('Welcome to Treasure Goblin! Press 1 to start or q to quit: ')
        if user_input != '1' and user_input != 'q':
            print(f'Please choose a valid option.')
        if user_input == 'q':
            print(f'Exiting, bye!')
            sys.exit()
        if user_input == '1':
            menu = False

    player_num_of_items = gen_num_of_items()
    print(f'Number of items to be generated: {player_num_of_items}')

main()
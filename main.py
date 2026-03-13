import random
import sys

PLAYER_ITEMS = {}

# generate a num between 1 and 5
def gen_num_of_items():
    return random.randint(1, 5)

def main():
    item_types = ['head', 'amulet', 'shoulders', 'chest', 'hands', 'belt', 'ring', 'legs', 'feet', 'weapon']
    quality_types = ['common', 'uncommon', 'magic', 'rare', 'unique']
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

    # the loop that runs X many times based on number of items
    for i in range(player_num_of_items):
        # pick the item type and quality
        print(f'Item: {random.choice(item_types)} and {random.choice(quality_types)}')

main()
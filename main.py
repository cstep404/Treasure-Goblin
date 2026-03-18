import random
import sys

PLAYER_ITEMS = {}

# generate a num between 1 and 5
def gen_num_of_items():
    return random.randint(1, 5)

def main():
    item_types = ['Helm', 'Amulet', 'Shoulders', 'Chest', 'Hands', 'Belt', 'Ring', 'Legs', 'Feet', 'Weapon']
    quality_types = ['Common', 'Uncommon', 'Magic', 'Rare', 'Unique']
    item_prefix = [
            'Colossus',
            'Defiant',
            'Heavenly',
            'Truthful',
            'Celestial'
    ]
    item_suffix = [
            'Scorn',
            'Intellect',
            'the Mountain',
            'the Knight',
            'the Druid'
    ]
    menu = True
    while menu:
        user_input = input('The Treasure Goblin cackles and says, "Ready for treasure? Press 1 to begin or q to quit!": ')
        if user_input != '1' and user_input != 'q':
            print(f'Please choose a valid option.')
        if user_input == 'q':
            print(f'Exiting, bye!')
            sys.exit()
        if user_input == '1':
            menu = False

    player_num_of_items = gen_num_of_items()

    # the loop that runs X many times based on number of items
    for i in range(player_num_of_items):
        # create a sub dict to add to player_items containing the item #, quality, and type
        PLAYER_ITEMS[f'Item {i + 1}'] = { 
            'Quality': random.choice(quality_types), 
            'Type': random.choice(item_types),
            'Prefix': random.choice(item_prefix),
            'Suffix': random.choice(item_suffix)
        }
        print(f'The Treasure Goblin laughs, "Here\'s you\'re reward!": {PLAYER_ITEMS[f'Item {i + 1}']['Prefix']} {PLAYER_ITEMS[f'Item {i + 1}']['Type']} of {PLAYER_ITEMS[f'Item {i + 1}']['Suffix']}, a {PLAYER_ITEMS[f'Item {i + 1}']['Quality']} quality item!')

    

main()
# Codey Webb
if __name__ == '__main__':
    def instructions():
        """Instructions for the player."""
        return ('\n   Instructions:\n'
                'To move between rooms, type \"Go [direction]\". Your movement options are North, South, East, or West.'
                '\nTo pick up an item, type \"Get [item name]\".'
                '\nTo exit the game, type \"Exit\".'
                '\nTo access this menu again, type \"Instructions\" or \"Help\".\n')


    def status(cur_location, cur_inventory):
        """Status of current location, inventory, room item if available, and available directions from current room are
        output."""
        room_options = []
        for option in list(rooms[cur_location].keys()):
            room_options.append(option)
        if 'Item' in room_options:
            room_options.remove('Item')
        if 'Item' in rooms[cur_location].keys():
            return ('\nYour current location: {}\n'
                    'Your Inventory: {}\n'
                    'You see the item: {}\n'
                    'You can go: {}\n'
                    'What do you want to do?\n  '.format(cur_location, cur_inventory, rooms[location].get('Item'),
                                                         ', '.join(room_options)))
        else:
            return ('Your current location: {}\n'
                    'Your Inventory: {}\n'
                    'You do not see an item\n'
                    'You can go: {}\n'
                    'What do you want to do?\n  '.format(cur_location, cur_inventory, ', '.join(room_options)))


    def go(cur_location, direction):
        """Move between rooms. If the room is kitchen, check inventory to count items for game win or loss."""
        if direction in list(rooms[cur_location].keys()):
            new_location = rooms[cur_location][direction]
            if new_location == 'Kitchen':
                new_location = 'Exit'
        return new_location


    def pickup(cur_location):
        """Add an item and delete the item key from that room in the rooms dictionary."""
        inventory.append(rooms[cur_location].get('Item'))
        del rooms[location]['Item']
        return inventory

    def endgame(inventory_items):
        if len(inventory_items) != 6:
            return print('\nYou didn\'t find all of the items you needed to go unnoticed! Your Grandma caught you red-'
                'handed and now you will not be allowed to have any pie for the rest of the night.')
        else:
            return print('\nYou have made it to the kitchen with everything you need and swiped the pie! Your Grandma '
                'suspects nothing yet. Let future you deal with the consequences while you enjoy your hard earned'
                ' pie.')


    rooms = {
        'Front Porch': {'East': 'Living Room'},
        'Living Room': {'North': 'Closet', 'South': 'Master Bedroom', 'East': 'Back Porch', 'West': 'Front Porch',
                        'Item': 'Sunglasses'},
        'Closet': {'South': 'Living Room', 'East': 'Laundry Room', 'Item': 'Bag'},
        'Laundry Room': {'West': 'Closet', 'Item': 'Batman Costume'},
        'Master Bedroom': {'North': 'Living Room', 'East': 'Master Bathroom', 'Item': 'Thick Socks'},
        'Master Bathroom': {'West': 'Master Bedroom', 'Item': 'Deodorant'},
        'Back Porch': {'North': 'Kitchen', 'West': 'Living Room', 'Item': 'Leather Gloves'},
        'Kitchen': {}
    }

    # The game story and objective
    print('\nAnything for pie! Your Grandma has told you that you cannot have any pie because it will \"ruin your '
        'appetite\". However, you\'re determined to get your hands on that pie while she busies herself making dinner.'
        ' In order to accomplish this, your goal is to pick up all of the items around the house in order to '
        'successfully sneak into the kitchen and swipe the pie. If you don\'t have all of the items, your Grandmother '
        'will easily spot you and you will lose the game. Once you reach the kitchen (with or without all of your '
        'items) or exit the game, the game will end. Good luck!')

    location = 'Front Porch'  # Starting location
    inventory = []  # Empty Inventory
    print(instructions())  # Instructions for the player

    while location != 'Exit':  # Game will continue until the Kitchen is reached or user inputs "Exit".
        print(status(location, inventory))  # Player and room information is output at the start of every loop.
        user_input = input().title().split()  # User input is split and changed to title case for program readability.
        if 'Go' in user_input[0] and user_input[1] in rooms[location].keys():
            if user_input[1] in rooms[location]:
                location = go(location, user_input[1])  # Go function is called to move between rooms
                if location == 'Kitchen':
                    location = 'Exit'
                    print(endgame(inventory))
        elif 'Get' in user_input[0]:
            if user_input[1] in rooms[location].get('Item'):
                inventory = pickup(location)  # Pickup function is called to pickup items
            else:
                print('That is not a valid item.')
        elif 'Instructions' or 'Help' in user_input[0]:
            print(instructions())
        elif 'Exit' in user_input[0]:
            location = 'Exit'
            print('\nYou have chosen to exit the game.')
        else:
            print('\nThat is not a valid command.')
    else:
        print('The game has ended.')

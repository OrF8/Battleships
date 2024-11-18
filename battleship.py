#################################################################
# FILE : battleship.py
# WRITER : Or Forshmit , or_forshmit8 , 327795464
# EXERCISE : intro2cs1 ex4 2024
# DESCRIPTION: A simple program that generates battleships game!
#################################################################

import helper


def ship_tiles():
    """A function that calculates the total length of ships"""
    total = 0
    for ship_size in helper.SHIP_SIZES:
        total += ship_size
    return total


# The total length of all ships
TOTAL_SHIP_TILES = ship_tiles()


def valid_coordinate(user_input):
    """A function that returns True if the coordinate is valid. Else, False"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # All letters in the alphabet
    if len(user_input) < 2:
        # The input must be a character and then a number,
        # so it's length must be at least 2
        return False
    if (not helper.is_int(user_input[1:]) or
        user_input[0].upper() not in letters):
        # If the input is not a character and then a number
        return False
    return True


def extract_column(loc):
    """A function that extracts the column index from loc tuple"""
    # In case the column index is bigger than 9
    column = 0
    for i in range(1, len(loc)):
        column += loc[i]
    return column


def valid_ship(board, size, loc):
    """A function that returns True is the ship is valid, False otherwise"""
    # If the number is negative or the character is not a letter
    if loc[0] < 0 or loc[1] < 0:
        return False
    for i in range(size):
        if loc[0] + i >= len(board) or loc[1] >= len(board[0]):
            # If this coordinate is bigger than the board
            return False
        if board[loc[0] + i][loc[1]] == helper.SHIP:
            # If the coordinate is already taken by a ship
            return False
    return True


def ship_locations(board, size):
    """A function that returns all the possible locations for placing ships"""
    locs = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if valid_ship(board, size, (i, j)):
                # Add the ship location only if it is valid
                if board[i][j] == helper.WATER:
                    locs.add((i, j))
    return locs


def torpedo_locations(board):
    """A function that returns all possible locations for firing torpedoes"""
    locs = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] != helper.HIT_SHIP and
                    board[i][j] != helper.HIT_WATER):
                # If we get here, this means that this location is not
                # a hit ship or a hit water location
                locs.add((i, j))
    return locs


def init_board(rows, columns):
    """A function that initializes an empty board"""
    board = []
    counter = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            # Make sure that the lists are not the same
            # If they are not the same, add WATER to it
            if len(board) == 0:
                row.append(helper.WATER)
                counter += 1
            if len(board) != 0 and row is not board[:counter]:
                row.append(helper.WATER)
                counter += 1
        board.append(row)
    return board


def cell_loc(name):
    """A function that returns a tuple that contains a coordinate"""
    return int(name[1:]) - 1, ord(name[0]) - 65


def place_battleship(board, size, loc):
    """A function that places a ship on the board in the desired coordinate"""
    for i in range(size):
        board[loc[0] + i][extract_column(loc)] = helper.SHIP


def create_player_board(rows, columns, ship_sizes):
    """A function that creates the player board and returns it"""
    # Initialize an empty board
    board = init_board(rows, columns)
    # If there are no ships to place
    if len(ship_sizes) == 0:
        return board
    # Iterate until all ships are placed:
    for ship_size in ship_sizes:
        placed = False
        while not placed:  # Iterate until the current ship has been placed
            helper.print_board(board)
            msg = f"Enter top coordinates for ship of size: {ship_size} "
            user_input = helper.get_input(msg).replace(' ', '')
            if valid_coordinate(user_input.upper()):
                # Get a number tuple coordinate
                loc = cell_loc(user_input.upper())
                # Iterate until the coordinate is valid:
                while not valid_ship(board, ship_size, loc):
                    print(f"Invalid location: {user_input.upper()}")
                    helper.print_board(board)
                    user_input = helper.get_input(msg).replace(' ', '')
                    if valid_coordinate(user_input.upper()):
                        # Get a number tuple coordinate
                        loc = cell_loc(user_input.upper())
                # If we get here, this means the coordinate is valid
                place_battleship(board, ship_size, loc)
                placed = True
            else:
                # If we get here, this means that the input is not valid
                print(f"Invalid input: '{user_input.upper()}'")
    return board


def create_pc_board(rows, columns, ship_sizes):
    """A function that creates the PC board and returns it"""
    # Initialize an empty board
    board = init_board(rows, columns)
    # If there are no ships to place
    if len(ship_sizes) == 0:
        return board
    # Iterate until all the ships are placed:
    for ship_size in ship_sizes:
        loc = helper.choose_ship_location(board, ship_size,
                                          ship_locations(board, ship_size))
        place_battleship(board, ship_size, loc)
    return board


def fire_torpedo(board, loc):
    """A function that fires a torpedo!"""
    column = extract_column(loc)
    # If location is not valid
    if loc[0] >= len(board) or column >= len(board[0]):
        return board
    # If location is a ship
    if board[loc[0]][column] == helper.SHIP:
        board[loc[0]][column] = helper.HIT_SHIP
    # If location is water
    elif board[loc[0]][column] == helper.WATER:
        board[loc[0]][column] = helper.HIT_WATER
    return board


def is_destroyed(board):
    """A function that returns True if the fleet has been destroyed"""
    # A counter that counts hit ship parts
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == helper.HIT_SHIP:
                # If there is a hit ship in this coordinate, add 1
                counter += 1
    if counter == TOTAL_SHIP_TILES:
        # If the number of hit ship parts is equal to the number of all ship
        # parts, this means that the whole fleet has been destroyed
        return True
    return False


def is_empty(board):
    """A function that returns True is the board is only WATER. Else, False"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != helper.HIT_WATER and board[i][j] != helper.WATER:
                return False
    return True


def valid_location(player_board, pc_board, loc):
    """A function that returns True if the location is valid. Else, False"""
    column = extract_column(loc)  # In case that the column is bigger than 9
    user_input = str(chr(int(loc[1]) + 65) + str(loc[0] + 1))
    # Iterate until it is a valid location:
    while (not valid_coordinate(user_input) or loc[0] >= len(pc_board) or
           column >= len(pc_board[0]) or column < 0 or loc[0] < 0):
        helper.print_board(player_board, pc_board)
        msg = f"Invalid target: {user_input}\nChoose target: "
        user_input = helper.get_input(msg).replace(' ', '').upper()
        if valid_coordinate(user_input.upper()):
            # If we get here, this means that the input is valid
            loc = cell_loc(user_input.upper())
            column = extract_column(loc)
    return loc


def unhit_location(player_board, pc_board, loc):
    """A function that returns True if the location was not hit. Else, False"""
    # Make sure that the coordinate is valid
    loc = valid_location(player_board, pc_board, loc)
    column = extract_column(loc)  # In case that the column is bigger than 9
    # Iterate until the location is unhit:
    while (pc_board[loc[0]][column] == helper.HIT_WATER or
           pc_board[loc[0]][column] == helper.HIT_SHIP):
        helper.print_board(player_board, pc_board)
        user_input = (helper.get_input("You have already hit this target."
                                       "\nChoose target: ")
                      .upper().replace(' ', ''))
        # Make sure the user input is valid:
        while not valid_coordinate(user_input):
            helper.print_board(player_board, pc_board)
            user_input = (helper.get_input(f"Invalid input: '{user_input}'"
                                           "\nChoose target: ")
                          .upper().replace(' ', ''))
        # If we get here, this means the coordinate is valid
        loc = valid_location(player_board, pc_board, cell_loc(user_input))
        column = extract_column(loc)
    return loc


def update_visible(visible, not_visible):
    """A function that updates the visible board"""
    # Visible and not visible have the same dimensions,
    # so we can iterate over only one's length
    for i in range(len(not_visible)):
        for j in range(len(not_visible[0])):
            if not_visible[i][j] == helper.HIT_WATER:
                visible[i][j] = helper.HIT_WATER
            elif not_visible[i][j] == helper.HIT_SHIP:
                visible[i][j] = helper.HIT_SHIP


def winner(player_board):
    """A function that announces the winner"""
    if is_empty(player_board) or is_destroyed(player_board):
        # If the player's board is destroyed or empty, he has lost
        return "lost :("
    # We call this function only after we know that at least one of the boards
    # is destroyed or empty, so if it is not the player's, it is the PC's
    return "won!"


def main():
    ans = 'Y'
    while ans != 'N':
        # Initialize the player board
        player_board = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS,
                                           helper.SHIP_SIZES)
        # Initialize an empty board that will hide the PC's board
        pc_board_visible = init_board(helper.NUM_ROWS, helper.NUM_COLUMNS)
        # Initialize the PC's real board
        pc_board_not_visible = create_pc_board(helper.NUM_ROWS,
                                               helper.NUM_COLUMNS,
                                               helper.SHIP_SIZES)
        # Print the player and PC boards
        helper.print_board(player_board, pc_board_visible)
        # Iterate until one or more fleet has been destroyed:
        while (not is_empty(player_board) and not is_destroyed(player_board)
               and not is_empty(pc_board_not_visible) and
               not is_destroyed(pc_board_visible)):
            # Player's turn:
            # Make sure that the location is valid and unhit
            user_input = helper.get_input("Choose target: ")
            # Make sure that the user input is valid:
            while not valid_coordinate(user_input.upper()):
                helper.print_board(player_board, pc_board_visible)
                user_input = helper.get_input(f"Invalid target: '{user_input}'"
                                              "\nChoose target: ")
            player_loc = unhit_location(player_board, pc_board_visible,
                                        cell_loc(user_input.upper().
                                                 replace(' ', '')))
            # PC's turn:
            pc_loc = helper.choose_torpedo_target(player_board,
                                                  torpedo_locations(
                                                      player_board))
            # Player fires the torpedo at a valid location
            fire_torpedo(pc_board_not_visible, player_loc)
            fire_torpedo(player_board, pc_loc)  # PC fires the torpedo
            # Update the PC's visible board
            update_visible(pc_board_visible, pc_board_not_visible)
            # Print the player and PC boards
            helper.print_board(player_board, pc_board_visible)
        # If we get here, this means that one or more boards has been destroyed
        ans = helper.get_input(f"You have {winner(player_board)}"
                               "\nWould you like to play again?"
                               "\nEnter 'Y' or 'N'. ")
        # Iterate until the player's input is valid
        while ans not in ['Y', 'N']:
            ans = helper.get_input("Your answer needs to be either 'Y' or 'N'."
                                   "\nwould you like to play again? ")


if __name__ == "__main__":
    main()

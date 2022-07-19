import time

# Initialize board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

count = 0
winner = False
play = True
tie = False
current_player = ''
player_details = []


def get_player_details(currentplayer):
    if currentplayer == 'A':
        return ['B', 'O']
    else:
        return ['A', 'X']


def print_board():
    for i in board:
        print(i, ':', board[i], ' ', end='')
        if i % 3 == 0:
            print()





def insert_input(slot_num, mark):
    while board[slot_num] != ' ':
        print("Mark cannot be placed in this spot")
        slot_num = int(input())
    board[slot_num] = mark


while play:

    print_board()

    player_details = get_player_details(current_player)
    current_player = player_details[0]
    print('The top row is 123, the middle row is 456, and the bottom row is 789')
    print("Player {}: Enter a number between 1 and 9".format(current_player))
    input_slot = int(input())

    insert_input(input_slot, player_details[1])
    count += 1


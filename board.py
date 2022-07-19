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


def check_win(mark, player_id):
    if board[1] == mark and board[2] == mark and board[3] == mark or \
            board[4] == mark and board[5] == mark and board[6] == mark or \
            board[7] == mark and board[8] == mark and board[9] == mark or \
            board[1] == mark and board[4] == mark and board[7] == mark or \
            board[2] == mark and board[5] == mark and board[8] == mark or \
            board[3] == mark and board[6] == mark and board[9] == mark or \
            board[1] == mark and board[5] == mark and board[9] == mark or \
            board[3] == mark and board[5] == mark and board[7] == mark:

        print_board()
        time.sleep(1)
        print("Player", player_id, "wins")
        return True

    else:
        return False


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

    winner = check_win(player_details[1], current_player)
    if winner:
        play = False
    if count == 9 and not winner:
        print("Tie")
        tie = True
        print_board()

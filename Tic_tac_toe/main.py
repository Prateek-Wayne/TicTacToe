game_still_going = True
winner = None
current_player = 'X'
# BOARD
board = ['-', '-', '-'
    , '-', '-', '-'
    , '-', '-', '-']


# DISPLAY A BOARD
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    global winner
    display_board()
    while game_still_going:
        handle_turn(current_player)
        game_state()
        flip_player()
    if winner == 'X' or winner == 'O':
        print(winner + ' WON\n')
    elif winner == None:
        print('TIE')
    game_state()


# TAKES INPUT
def handle_turn(player):
    print(player + " 's turn")
    position = input('choose a position from 1 to 9->\n')
    valid =False
    while not valid:
        while position not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            position = input('CHOOSE A VALID INPUT from 1-9:- ')
        position = int(position) - 1
        if board[position] == '-':
            valid=True
        else:
            print("YOU CAN'T GO THERE::,,GO AGAIN")

    board[position] = player
    display_board()


# CHECKS GAME'S STATE:TIE ,WIN
def game_state():
    check_win()
    check_TIE()

# CHECK FOR TIE
def check_TIE():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

# CHECK FOR WIN
def check_win():
    global winner
    row_win = check_row()
    coloumn_win = check_coloumn()
    diagonal_win = check_diagonal()
    if row_win:
        winner = row_win
    elif coloumn_win:
        winner = coloumn_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_row():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    # return


def check_coloumn():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    # return


def check_diagonal():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[6] == board[4] == board[2] != '-'

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    # return


# SWITCH THE PLAYERS
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()

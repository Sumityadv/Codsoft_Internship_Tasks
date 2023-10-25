import copy

Layout = [' ' for _ in range(9)]                                              # this is game layout
Player = 'X'
Bot = 'O'

def empty_cells(Layout):                                                      #this function will only check empty spaces if there is any free slot or not
    return [i for i, val in enumerate(Layout) if val == ' ']

def print_Layout(Layout):
    for row in [Layout[i:i+3] for i in range(0, 9, 3)]:                      #this function will make tic tac toe game layout
        print(' | '.join(row))
        print('-' * 9)

def check_win(Layout, player):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),                                  #this function will tell if player or bot wins or not
                        (0, 4, 8), (2, 4, 6))
    return any(all(Layout[i] == player for i in combo) for combo in win_combinations)

def best_move(Layout):
    best_eval = -float('inf')
    best_move = -1

    for move in empty_cells(Layout):
        Layout_copy = copy.deepcopy(Layout)
        Layout_copy[move] = Bot                                                        # this function uses minimax and find best move for bot to win the game
        eval = minimax(Layout_copy, 9, False)
        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move


def minimax(Layout, depth, maximizing_player):
    if check_win(Layout, Bot):
        return 1
    if check_win(Layout, Player):                                                       # we have used minimax algorithm with alpha beta pruning to check best possible outcomes 
        return -1                                                                       # after every move and if bot wins it return 1 and if player wins it return 1 and if its a tie then it retun 0
    if not empty_cells(Layout):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for move in empty_cells(Layout):
            Layout_copy = copy.deepcopy(Layout)
            Layout_copy[move] = Bot
            eval = minimax(Layout_copy, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in empty_cells(Layout):
            Layout_copy = copy.deepcopy(Layout)
            Layout_copy[move] = Player
            eval = minimax(Layout_copy, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

while True:
    print_Layout(Layout)
    if empty_cells(Layout):
        Player_move = int(input("Enter your move (0-8): "))
        if 0 <= Player_move < 9 and Layout[Player_move] == ' ':
            Layout[Player_move] = Player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(Player):                                                       # this function will be the real time game loop where playing occurs
            print_Layout(Layout)
            print("Player wins!")
            break
    else:
        print("It's a draw!")
        break

    Bot_move = best_move(Layout)
    Layout[Bot_move] = Bot

    if check_win(Layout, Bot):
        print_Layout(Layout)
        print("Bot wins!")
        break

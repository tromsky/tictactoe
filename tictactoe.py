"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

# from turtle import pd

X = "X"
O = "O"
EMPTY = None

# testing states
first = [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
second = [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, O]]
second_last = [[X, O, X], [O, X, O], [X, O, EMPTY]]
last = [[X, O, X], [O, X, O], [X, O, X]]
first_win = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, O]]
second_win = [[X, X, O], [O, O, O], [EMPTY, EMPTY, O]]
third_win = [[X, O, X], [EMPTY, EMPTY, EMPTY], [O, O, O]]
fourth_win = [[X, X, O], [X, EMPTY, EMPTY], [X, EMPTY, O]]
fifth_win = [[O, X, X], [EMPTY, X, EMPTY], [EMPTY, X, O]]
seventh_win = [[X, X, O], [EMPTY, EMPTY, O], [EMPTY, EMPTY, O]]
eigth_win = [[X, X, O], [EMPTY, X, O], [EMPTY, EMPTY, X]]
ninth_win = [[O, X, X], [EMPTY, X, O], [X, EMPTY, O]]


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # set up some variables to track the counts
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if o_count < x_count:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for row_position, row in enumerate(board):
        for cell_position, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((row_position, cell_position))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_state = deepcopy(board)

    if action not in actions(board):
        raise ValueError("Action is not valid for board state")

    # player_turn = player(board_state)

    row_position, cell_position = action

    board_state[row_position][cell_position] = player(board)

    return board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # top row
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] is not EMPTY:
        return board[0][0]

    # middle row
    if (board[1][0] == board[1][1] == board[1][2]) and board[1][0] is not EMPTY:
        return board[1][0]

    # bottom row
    if (board[2][0] == board[2][1] == board[2][2]) and board[2][0] is not EMPTY:
        return board[2][0]

    # left column
    if (board[0][0] == board[1][0] == board[2][0]) and board[0][0] is not EMPTY:
        return board[0][0]

    # middle column
    if (board[0][1] == board[1][1] == board[2][1]) and board[0][1] is not EMPTY:
        return board[0][1]

    # right column
    if (board[0][2] == board[1][2] == board[2][2]) and board[0][2] is not EMPTY:
        return board[0][2]

    # horizontal, top-left to bottom-right
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not EMPTY:
        return board[0][0]

    # horizontal, top-right to bottom-left
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] is not EMPTY:
        return board[2][0]

    # no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # if there are no actions left to take or the board has a winner,
    # it is terminal
    if actions(board) is None or winner(board) is not None:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) is X:
        return 1

    if winner(board) is O:
        return -1

    # tie, or no winner on a terminal board
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

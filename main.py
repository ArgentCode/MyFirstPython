import random
import sys

board = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "]
]


def game_lose_check():
    global board
    for row in board:
        for col in row:
            if col != " ":
                return False
    return True


def add_number():
    global board
    rand1 = random.randint(0, 3)
    rand2 = random.randint(0, 3)
    while board[rand1][rand2] != " ":
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
    board[rand1][rand2] = "2"


def print_board():
    global board
    for row in board:
        print(row)


def shift(user):
    if user == "up":
        print("up detected")
        for row in range(0, 4):
            for col in range(0, 4):
                row_temp = row
                while board[row][col] != " " and row-1 >= 0 and board[row-1][col] == " ":
                    board[row-1][col] = board[row][col]
                    board[row][col] = " "
                    row -= 1
                row = row_temp
    if user == "down":
        print("down detected")
        for row in range(4, 0, -1):
            for col in range(0, 4):
                print(str(row) + ": " + str(col))
                row_temp = row
                while row+1 <= 4 and board[row][col] != " " and board[row+1][col] == " ":
                    board[row+1][col] = board[row][col]
                    board[row][col] = " "
                    row += 1
                row = row_temp


def __main__():
    add_number()
    add_number()
    print_board()
    while not game_lose_check():
        user = input("Would you like to go up, down, right or left: ")
        if user == "c":
            return
        print("--------------------")
        shift(user.lower().strip())
        print_board()


__main__()
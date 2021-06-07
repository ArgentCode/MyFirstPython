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
    for row in range(0, 4):
        for col in range(0, 4):
            if board[row][col] == " ":
                return False
    return True


def win_check(number):
    if number == 2048:
        print("You win!")
        sys.exit()


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
                if row-1 >= 0 and board[row][col] != " " and board[row-1][col] == board[row][col]:
                    number = int(board[row-1][col]) * 2
                    board[row-1][col] = str(number)
                    board[row][col] = " "
                    win_check(number)
                row = row_temp
    if user == "down":
        print("down detected")
        for row in range(3, -1, -1):
            for col in range(0, 4):
                row_temp = row
                while row+1 < 4 and board[row][col] != " " and board[row+1][col] == " ":
                    board[row+1][col] = board[row][col]
                    board[row][col] = " "
                    row += 1
                if row+1 < 4 and board[row][col] != " " and board[row+1][col] == board[row][col]:
                    number = int(board[row+1][col]) * 2
                    board[row+1][col] = str(number)
                    board[row][col] = " "
                    win_check(number)
                row = row_temp
    if user == "right":
        print("right detected")
        for row in range(0, 4):
            for col in range(4, -1, -1):
                col_temp = col
                while col+1 < 4 and board[row][col] != " " and board[row][col+1] == " ":
                    board[row][col+1] = board[row][col]
                    board[row][col] = " "
                    col += 1
                if col+1 < 4 and board[row][col] != " " and board[row][col+1] == board[row][col]:
                    number = int(board[row][col+1]) * 2
                    board[row][col+1] = str(number)
                    board[row][col] = " "
                    win_check(number)
                col = col_temp
    if user == "left":
        print("left detected")
        for row in range(0, 4):
            for col in range(0, 4):
                col_temp = col
                while col-1 >= 0 and board[row][col] != " " and board[row][col-1] == " ":
                    board[row][col-1] = board[row][col]
                    board[row][col] = " "
                    col -= 1
                if col-1 >= 0 and board[row][col] != " " and board[row][col-1] == board[row][col]:
                    number = int(board[row][col-1]) * 2
                    board[row][col-1] = str(number)
                    board[row][col] = " "
                    win_check(number)
                col = col_temp


def __main__():
    add_number()
    add_number()
    print_board()
    while not game_lose_check():
        user = input("Would you like to go up, down, right or left: ")
        if user.lower().strip() == "c":
            print("End of test")
            return
        print("--------------------")
        shift(user.lower().strip())
        add_number()
        print_board()
    print("Sorry you lost!")


__main__()
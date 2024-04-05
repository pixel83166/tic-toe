import colorama
import os

clear = lambda: os.system('cls')
colorama.init()

white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
red_color = colorama.Fore.RED
blue_color = colorama.Fore.BLUE

board = list(range(0, 9))
cells = 3
dashes = 13

spacec = 14
counter = 0
is_win = False
win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

player_token = ""

print(green_color + "Tic-tac toe the games for two players. ")

while not is_win:
    for i in range(cells):
        print(blue_color + " " * spacec, end="")
        print(blue_color + "-" * dashes)
        print(' ' * spacec, end='')
        print(
            f"{blue_color}| {white_color}{board[0 + i * 3]} {blue_color}|{white_color} {board[1 + i * 3]}{blue_color} |{blue_color} {white_color}{board[2 + i * 3]}{blue_color} |")
        print(' ' * spacec, end='')
        print(blue_color + "-" * dashes)

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = "O"

    is_valid = False
    while not is_valid:
        player_answer = input(f"Where we put a {player_token}?: ")
        try:
            player_answer = int(player_answer)
        except:
            print("Invailed input. A number expected")
            continue
        if 0 <= player_answer <= 8:
            if str(board[player_answer]) not in "XO":
                board[player_answer] = player_token
                is_valid = True
            else:
                print(f"{red_color}This cell is arleady taken!")
                continue
    clear()
    counter += 1

    if counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            print(f'{green_color}{player_token} is win!')

    if counter == 9:
        print(green_color + "Draw! You're amazing!")
        break
for i in range(cells):
    print(blue_color + " " * spacec, end="")
    print(blue_color + "-" * dashes)
    print(' ' * spacec, end='')
    print(
        f"{blue_color}| {white_color}{board[0 + i * 3]} {blue_color}| {white_color}{board[1 + i * 3]}{blue_color} | {white_color}{board[2 + i * 3]}{blue_color} |")
    print(' ' * spacec, end="")
    print(blue_color + "-" * dashes)

input(white_color + 'Press the Enter to exit.')
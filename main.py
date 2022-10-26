import emoji
from art import *
from colorama import *


board = list(range(1, 10))


def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|',
              board[0 + i * 3],
              '|',
              board[1 + i * 3],
              '|',
              board[2 + i * 3],
              '|')
        print('-' * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(Fore.YELLOW
                              + 'Куда поставим ' + player_token
                              + '? ' + Style.RESET_ALL)
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in (x, o)):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('\n' + 'Эта клетка занята' + '\n')
        else:
            print('Некорректный ввод.'
                  'Введите число от 1 до 9 чтобы совершить ход.')


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(x)
        else:
            take_input(o)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'выиграл!' + emoji.emojize(':trophy:'))
                print(text2art('victory'))
                win = True
                exit()
        if counter == 9:
            print(emoji.emojize(':handshake_light_skin_tone:') + 'Ничья!')
            exit()
    draw_board(board)


init()
print(Back.GREEN + '_tic-tac-toe_' + Style.RESET_ALL)
x = Fore.RED + 'X' + Style.RESET_ALL
o = Fore.BLUE + 'O' + Style.RESET_ALL
main(board)

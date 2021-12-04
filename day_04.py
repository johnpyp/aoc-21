import re
import aoc_helper

real_raw = aoc_helper.fetch(4, 2021)
test_raw = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".strip()

raw = real_raw


def parse_raw():

    input_sections = raw.split("\n\n")
    order = list(map(int, input_sections[0].split(",")))
    raw_boards = input_sections[1:]

    boards = []
    for raw_board in raw_boards:
        board = []
        for l in raw_board.splitlines():
            clean_line = re.sub(r"\s+", " ", l.strip())
            board.append(list(map(int, clean_line.split(" "))))
        boards.append(board)

    return order, boards


def check_board(board):
    for i in range(len(board)):
        c = 0
        for j in range(len(board[0])):
            cell = board[i][j]
            if cell == -1:
                c += 1
        if c == 5:
            return True

    for j in range(len(board[0])):
        c = 0
        for i in range(len(board)):
            cell = board[i][j]
            if cell == -1:
                c += 1
        if c == 5:
            return True
    c = 0
    for i in range(5):
        cell = board[i][i]
        if cell == -1:
            c += 1
    if c == 5:
        return True

    c = 0
    for i in range(5):
        cell = board[i][-i]
        if cell == -1:
            c += 1
    if c == 5:
        return True

    return False


def apply_guess(n, boards):
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board)):
                cell = board[i][j]
                if cell == n:
                    board[i][j] = -1


def sum_uncounted(board):
    c = 0
    for i in range(len(board)):
        for j in range(len(board)):
            cell = board[i][j]
            if cell != -1:
                c += cell
    return c


def part_one():
    order, boards = parse_raw()
    print(boards)
    for guess in order:
        apply_guess(guess, boards)
        for board_idx, board in enumerate(boards):
            is_valid = check_board(board)
            if is_valid:
                print(sum_uncounted(board), guess)
                return sum_uncounted(board) * guess

    return -1


def part_two():
    order, boards = parse_raw()
    print(boards)
    won_boards = [False] * len(boards)

    win_c = 0
    for guess in order:
        apply_guess(guess, boards)
        for board_idx, board in enumerate(boards):
            if won_boards[board_idx] == True:
                continue
            is_valid = check_board(board)
            if is_valid:
                win_c += 1
                won_boards[board_idx] = True
                if win_c == len(boards):
                    print(board_idx, sum_uncounted(board), guess)
                    return sum_uncounted(board) * guess

    return -1


print("PART ONE", part_one())
print("PART TWO", part_two())

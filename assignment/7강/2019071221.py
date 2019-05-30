# -*- coding: utf-8 -*-
import random

def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    sprout = [seed[3], seed[4], seed[5], seed[0], seed[1], seed[2]]
    stem = [seed[2], seed[0], seed[1], seed[5], seed[3], seed[4]]
    flower = [seed[5], seed[3], seed[4], seed[2], seed[0], seed[1]]
    death = [seed[1], seed[2], seed[0], seed[4], seed[5], seed[3]]
    continuity = [seed[4], seed[5], seed[3], seed[1], seed[2], seed[0]]
    board = [seed, sprout, stem, flower ,death ,continuity ]
    return board

def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for x in range(len(board)):
            transposed[x] += [row[x]]
    return transposed

def shuffle_ribbons_1(board):
    top = board[:2]
    middle = board[2:4]
    bottom = board[4:]
    random.shuffle(top)
    random.shuffle(middle)
    random.shuffle(bottom)
    return top + middle + bottom

def shuffle_ribbons_2(board):
    top = board[:3]
    bottom = board[3:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def create_solution_board():
    board = create_board()
    board = shuffle_ribbons_1(board)
    board = transpose(board)
    board = shuffle_ribbons_2(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == '하':
        return 15
    if level == '중':
        return  18
    if level == '상':
        return  21

def make_holes(board,no_of_holes):
    holeset=set()
    while no_of_holes > 0:
        i= random.randint(0,5)
        j= random.randint(0,5)
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -=1
        else:
            continue
    return (board, holeset)


def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        for x in range(len(board)):
            if row[x] == 0:
                row[x] = '.'
        print(i, '|', str(row[0]),str(row[1]),str(row[2]),str(row[3]), str(row[4]), str(row[5]))
        i += 1
    print()

def get_integer(message,i,j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <=j):
        number = input(message)
    return int(number)

def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle, holeset) = make_holes(puzzle, no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0 :
        i = get_integer("가로줄번호(1-6): ",1,6) -1
        j = get_integer("세로줄번호(1-6): ",1,6) -1
        if (i,j) not in holeset:
            print('빈칸이 아닙니다.')
            continue
        n = get_integer('숫자(1-6): ',1,6)
        sol=solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -=1
        else:
            print(n, '가 아닙니다. 다시 시도해보세요.')
    print('잘 하셨습니다. 또 들려주세요.')

sudokmini()

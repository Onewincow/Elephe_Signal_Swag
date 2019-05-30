import random
def make_holes(board,no_of_holes):
    holeset=set()
    while no_of_holes > 0:
        i= random.randint(0,3)
        j= random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -=1
        else:
            continue
    return (board, holeset)

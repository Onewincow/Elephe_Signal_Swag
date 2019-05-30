

def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for x in range(len(board)):
            transposed[x] += [row[x]]
    return transposed

board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transpose(board))


def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board():
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

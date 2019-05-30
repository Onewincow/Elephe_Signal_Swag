# -*- coding: utf-8 -*-
def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
    i = 1
    for row in board:
        for x in range(len(board)):
            if row[x] == 0:
                row[x] = '.'
        print(i, '|', str(row[0]),str(row[1]),str(row[2]),str(row[3]))
        i += 1
    print()
show_board([[0,3,0,0],[2,4,0,0],[3,1,2,0],[0,2,1,0]])

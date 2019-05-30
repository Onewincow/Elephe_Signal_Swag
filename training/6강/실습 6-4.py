def transpose(mat):
    no_of_columns = len(mat[0])
    transposed = []
    for i in range(no_of_columns):
        list = []
        for j in range(len(mat)):
            list += [mat[j][i]]
        transposed += [list]
    return transposed
print(transpose([[1,2,5],[3,4,6]]))

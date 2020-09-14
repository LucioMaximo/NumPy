import numpy as np
from functools import reduce
# this version has no comments to make it quicker.
iterations = 0


def sudoku_solver(updatedsudo):
    global iterations
    iterations += 1
    zrow, zcolumn = np.asarray(updatedsudo == 0).nonzero()
    if zrow.size == 0:
        print(iterations)
        return True, updatedsudo
    zrow, zcolumn = zrow[0], zcolumn[0]
    square = updatedsudo[zrow//3*3:zrow//3*3+3, zcolumn//3*3:zcolumn//3*3+3].reshape(1, 9)
    row = updatedsudo[zrow, :]
    col = updatedsudo[:, zcolumn]
    numbers = np.arange(1, 10)
    poss = np.setdiff1d(numbers, reduce(np.union1d, (row, col, square)))
    sudotest = np.copy(updatedsudo)
    for cposs in poss:
        sudotest[zrow, zcolumn] = cposs
        recursive = sudoku_solver(sudotest)
        if recursive[0]:
            return recursive
    return False, None


solve = np.array  ([[0, 0, 0, 0, 0, 4, 9, 2, 0],
                    [0, 0, 0, 9, 0, 0, 4, 0, 0],
                    [0, 0, 0, 0, 3, 0, 8, 0, 7],
                    [0, 0, 8, 0, 0, 9, 1, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0, 4, 0],
                    [0, 0, 6, 1, 0, 0, 7, 0, 0],
                    [6, 0, 4, 0, 5, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 3, 0, 0, 0],
                    [0, 8, 9, 4, 0, 0, 0, 6, 0]])

print(sudoku_solver(solve))

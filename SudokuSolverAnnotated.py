import numpy as np
from functools import reduce

iterations = 0

# back tracking recursive function
def sudoku_solver(updatedsudo):
    global iterations
    iterations += 1

    zrow, zcolumn = np.asarray(updatedsudo == 0).nonzero()  # store column and row locations of every 0 into two arrays
    # remove array names etc by storing the 0 locations into two vars zrow and zcolumn
    # print("Zrow: "+str(zrow)+"Zcolumn: "+str(zcolumn))
    if zrow.size == 0:  # if there are no 0s left
        print(iterations)  # print the amount of iterations required to solve
        return True, updatedsudo  # if there are no 0s left, return true and return the finished sudoku.
    # below we will iterate through until there are no 0s left solving the sudoku as we go
    zrow, zcolumn = zrow[0], zcolumn[0]  # go to the first 0
    square = updatedsudo[zrow//3*3:zrow//3*3+3, zcolumn//3*3:zcolumn//3*3+3].reshape(1, 9)
    # make an array to dynamically index the square containing the current 0
    row = updatedsudo[zrow, :]  # make and array to index the row for the current 0
    # col = updatedsudo[:, zcolumn].reshape(9,1)
    col = updatedsudo[:, zcolumn]  # make an array to index the column for the current 0
    numbers = np.arange(1, 10)  # local var array 1-9 to be used later for calculations,
    poss = np.setdiff1d(numbers, reduce(np.union1d, (row, col, square)))
    # a lot going on here - usually we can use union 1d on 2 arrays, but we need to use reduce() AND union 1d to be
    # able to compare arrays. It uses the 3 arrays I declared above and gets all values that are common between them.
    # finally, settdif1d compares those numbers with the 1-9 numbers declared at the start, returning the possible
    # numbers that could be in that position, based off of the current state of the sudoku.
    # also, when recursively called below, when there aren't any possibilities left i.e. poss = 0, this will
    # cause that branch of the loop to abandon, where it will resume with the second number of a previous poss array.
    # and continue branching down the possible remaining options.

    sudotest = np.copy(updatedsudo)  # make a copy of the current sudoku

    for cposs in poss:   # for loop using the possible values that this current 0 could be

        sudotest[zrow, zcolumn] = cposs  # set 0 in the sudoku grid to the possible value
        recursive = sudoku_solver(sudotest)  # recursively call using the copied updated version of the sudoku.
        # creates up to thousands of branches of possible solutions to the puzzle, when it is confirmed above that
        # the current solution is false, due to line ~23 returning an empty set, the recursive loop branches back up
        # for however many times that it is nested that there are still possibilities above it, until all combinations
        # are expended.

        if recursive[0]:  # i.e if a solution is found (if recursive[0] == true)

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

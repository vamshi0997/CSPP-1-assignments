'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in sudoku:
        for j in i:
            if int(j) >= 1 and int(j) <= 9:
                num = i.count(j)
                if num > 1:
                    return False
            else:
                return False
    i = 0
    while i < 9:
        list1 = []
        for j in range(9):
            list1 = list1 + [sudoku[j][i]]
        for k in list1:
            if  int(k) >= 1 and int(k) <= 9:
                num = list1.count(k)
                if num > 1:
                    return False
            else:
                return False
        i = i + 1


    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        i = i + 1
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()

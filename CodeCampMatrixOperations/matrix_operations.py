'''this is matrix program'''
import numpy
def mult_matrix(matrix1, matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    rows = numpy.shape(matrix1)
    columns = numpy.shape(matrix2)
    matrix3 = [[0]*columns[1] for i in range(rows[0])]
    if rows[1] == columns[0]:
        for i in range(rows[0]):
            for j in range(columns[1]):
                for k in range(columns[0]):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        return matrix3
    
    print("Error: Matrix shapes invalid for mult")
    return None


def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''

    rows = numpy.shape(matrix1)
    columns = numpy.shape(matrix2)
    matrix3 = [[0]*columns[1] for i in range(rows[0])]
    if rows == columns:
        for i in range(rows[0]):
            for j in range(columns[1]):
                matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        return matrix3
    
    print("Error: Matrix shapes invalid for addition")
    return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows, columns = [int(j) for j in input().split(",")]
    list1 = []
    for i in range(rows):
        i = i + 1
        list2 = [int(k) for k in input().split(" ")]
        if len(list2) != columns:
            print("Error: Invalid input for the matrix")
            return None
        list1.append(list2)
    return list1

def main():
    '''# read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2'''
    matrix1 = read_matrix()
    matrix2 = read_matrix()
    if (matrix1 != None and matrix2 != None):
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2))

if __name__ == '__main__':
    main()

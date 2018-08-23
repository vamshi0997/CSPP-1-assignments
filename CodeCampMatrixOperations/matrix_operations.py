import numpy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    n1 = numpy.shape(m1)
    n2 = numpy.shape(m2)
    matrix3 = [[0]*n2[1] for i in range(n1[0])]
    if n1[1] == n2[0]:
        for i in range(n1[0]):
            for j in range(n2[1]):
                for k in range(n2[0]):
                    matrix3[i][j] += m1[i][k] * m2[k][j]
        return matrix3
    else:
        print("Error: Matrix shapes invalid for mult")
        return None


def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    n1 = numpy.shape(m1)
    n2 = numpy.shape(m2)
    matrix3 = [[0]*n2[1] for i in range(n1[0])]
    if n1 == n2:
            for i in range(n1[0]):
                for j in range(n2[1]):
                    matrix3[i][j] = m1[i][j] + m2[i][j]
            return matrix3
    else:
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
    n1, n2 = [int(j) for j in input().split(",")]
    list1 = []
    for i in range(n1):
        list2 = [int(k) for k in input().split(" ")]
        if len(list2)!= n2:
            print("Error: Invalid input for the matrix")
            return
        list1.append(list2)
    return list1


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix1 = read_matrix()
    matrix2 = read_matrix()
    if (matrix1 != None and matrix2 != None):
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2))
    
if __name__ == '__main__':
    main()

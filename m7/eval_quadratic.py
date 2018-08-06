'''# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x)
#that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.'''


def evalquadratic(a1_, b1_, c1_, x1_):
    ''' give the four inputs'''
    return a1_*x1_**2+b1_*x1_+c1_

def main():
    ''' you are in main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    le_ = len(data)
    for x1_ in range(le_):
        temp = str(data[x1_]).split('.')
        if temp[1] == '0':
            data[x1_] = int(float(str(data[x1_])))
        else:
            data[x1_] = data[x1_]
    print(evalquadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()

'''# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x)
#that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.'''


def evalQuadratic(aaa, bbb, ccc, xen):
    ''' give the four inputs'''
    return aaa*xen**2+bbb*xen+ccc
    

def main():
    ''' you are in main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x in range(len(data)):
        temp = str(data[xen]).split('.')
        if(temp[1] == '0'):
            data[xen] = int(float(str(data[xen])))
        else:
            data[xen] = data[xen]
    print(evalQuadratic(data[0],data[1],data[2],data[3]))

if __name__ == "__main__":
	main()

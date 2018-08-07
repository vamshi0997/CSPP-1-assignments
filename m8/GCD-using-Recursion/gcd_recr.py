'''# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b)
#that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.'''


def gcdrecur_(a1_, b1_):
    '''a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a1_ == 0 or b1_ == 0:
        return 0
    elif a1_ == 1 or b1_ == 1:
        return 1
    elif a1_ > b1_:
        return gcdrecur_(b1_, a1_-b1_)
    elif a1_ == b1_:
        return a1_
    return gcdrecur_(a1_, b1_-a1_)

def main():
    ''' give the inputs to find their gcd'''
    data = input()
    data = data.split()
    print("GCD is:", gcdrecur_(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()

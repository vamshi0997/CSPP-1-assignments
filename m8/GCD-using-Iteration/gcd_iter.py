'''# Exercise: GCDIter
# Write a Python function, gcdIter(a, b)
#that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.'''


def gcditer_(a1_, b1_):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while a1_ >= 0 and b1_ >= 0:
        if a1_ == 0 or b1_ == 0:
            return 0
        elif a1_ == 1 or b1_ == 1:
            return 1
        elif a1_ > b1_:
            b1_ = a1_%b1_
            a1_ = b1_
        elif a1_ == b1_:
            return a1_
        elif a1_ < b1_:
            a1_ = b1_%a1_
            b1_ = a1_
        return gcditer_(a1_, b1_)

def main():
    ''' you are in main function'''
    data = input()
    data = data.split()
    print("GCD is:", gcditer_(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()

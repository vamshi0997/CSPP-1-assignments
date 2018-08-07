'''# Exercise: Assignment-2
# Write a Python function, sumofdigits,
#that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.'''


def sumofdigits(n1_):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    sum1 = 0
    while n1_ >= 1:
        rem = n1_%10
        sum1 = sum1+rem
        n1_ = n1_//10
    return sum1


def main():
    '''
    a is positive integer
    '''
    a1_ = input()
    print(sumofdigits(int(a1_)))

if __name__ == "__main__":
    main()

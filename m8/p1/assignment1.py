'''# Exercise: Assignment-1
# Write a Python function, factorial(n),
#that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.'''


def factorial(n1_):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n1_ == 0:
        return 1
    elif n1_ == 1:
        return 1
    return n1_*factorial(n1_-1)

def main():
    ''' you are in main function'''
    a1_ = input()
    print(factorial(int(a1_)))

if __name__ == "__main__":
    main()

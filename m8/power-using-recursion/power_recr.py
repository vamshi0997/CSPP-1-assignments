'''# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp),
that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.'''


def recurpower_(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1
    return base*recurpower_(base, exp-1)

def main():
    ''' you are in main function'''
    data = input()
    data = data.split()
    print(recurpower_(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()

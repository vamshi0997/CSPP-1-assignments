'''# Exercise: odd

# Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.'''


def odd(X1):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    if X1%2 != 0:
    	return True
    else:
    	return False

    

def main():
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()

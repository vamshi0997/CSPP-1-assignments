'''# Write a python program to find the square root of the given number
# using Newton rapson method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    ''' your in main function'''
    new = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    guess = new/2.0
    # your code starts here
    while abs(guess*guess - new) >= epsilon:
        guess = guess - (((guess**2) - new)/ (2*guess))
    print(str(guess))

if __name__ == "__main__":
    main()

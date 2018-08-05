''' # Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991 '''

def main():
    '''you are in main method'''
    approx = int(input())
    # epsilon and step are initialized
	# don't change these values
    epsilon = 0.01
    step = 0.1
    # your code starts here
    guess = 0.0
    num_guesses = 0
    while abs(guess**2 - approx) >= epsilon and guess <= approx:
        guess += step
        num_guesses += 1
    if abs(guess**2 - approx) >= epsilon:
        print("Failed on square root of", approx)
    else:
        print(guess)

if __name__ == "__main__":
    main()

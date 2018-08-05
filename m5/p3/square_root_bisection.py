'''# Write a python program to find the square root of the given number
# using bisection method method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    ''' you in main functio '''
    guess = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    # your code starts here
    low = 0.0
    high = guess
    ans = (high + low)/2.0
    while abs(ans**2 - guess) >= epsilon:
        if ans**2 < guess:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print(ans)

if __name__ == "__main__":
    main()

'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''

def main():
    ''' This is guess program'''
    # input is captured in s
    guess = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    ans = 0
    neg_flag = False
    if guess < 0:
        neg_flag = True
    while ans**3 < guess:
        ans += 1
    if ans**3 == guess:
        print(guess, "is a perfect cube")
    else:
        print(guess, "is not a perfect cube")
        if neg_flag:
            print("Just checking ... did you mean", -guess, "?")

if __name__ == "__main__":
    main()

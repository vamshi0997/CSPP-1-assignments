'''# Exercise: Is In
# Write a Python function, isIn(char, aStr),
#that takes in two arguments a character and String and returns the isIn(char, aStr)
#which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.'''

def isin_(char, str1_):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    le_ = len(str1_)
    if le_ == 0:
        return False
    elif le_ == 1:
        return str1_ == char
    elif str1_[le_//2] == char:
        return True
    elif ord(str1_[le_//2]) > ord(char):
        return isin_(char, str1_[:le_//2])
    return isin_(char, str1_[le_//2:le_])

def main():
    ''' you are in main function'''
    data = input()
    data = data.split()
    print(isin_((data[0][0]), data[1]))


if __name__ == "__main__":
    main()

'''Assume s is a string of lower case characters.
    Write a program that prints the number of times the string 'bob' occurs in s.
    For example, if s = 'azcbobobegghakl', then your program should print
    Number of times bob occurs is: 2'''

def main():
    ''' inside main '''
    str_ = input('')
    # the input string is in s
    # remove pass and start your code here
    str1_ = 'bob'
    le_ = len(str_)
    count_ = 0
    for i in range(le_):
        if str_[i:i+3] == str1_:
            count_ += 1
    print(count_)

if __name__ == "__main__":
    main()

'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''
    function for cleaning up the string'''
    str = ""
    for i in string:
        if i.isalnum() is True:
            str = str + i
    return str

def main():
    '''
    string: input is a string.'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    k = str()
    for i in str_input:
        if i in ('!', '@', '#', '%', '$', '^', '&', '*'):
            k = k + " "
        else:
            k = k + i
    print(k)


if __name__ == "__main__":
    main()

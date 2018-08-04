'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    num = str(int_input)
    product = 1
    for i in num:
        if i != '-':
            temp = int(i)
            product = product*temp
        else:
            temp = int(i)
            
            

            
    print(product)


if __name__ == "__main__":
    main()

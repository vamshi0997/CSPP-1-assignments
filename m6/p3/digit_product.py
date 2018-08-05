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
    num = int(input())
    product = 1
    if num >= 1:
        while num > 1:
            rem = num%10
            print(rem)
            num = int(num/10)
            print(num)
            product = product*rem
            print(product)
        print(product)
    elif num == 0:
        print(0)
    else:
        num = -(num)
        while num > 1:
            rem = num%10
            num = int(num/10)
            product = product*rem
        print(-product)




if __name__ == "__main__":
    main()

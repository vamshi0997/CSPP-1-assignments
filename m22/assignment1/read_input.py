'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	'''
	num: integer for number of lines.'''
    num = int(input())
    i = 0
    while i < num:
    	print(input())
    	i = i + 1

if __name__ == '__main__':
    main()

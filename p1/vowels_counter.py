#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    s_= input()
	# the input string is in s
	# remove pass and start your code here
    c_= 0
    for i in s_:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            c_=c+1
    print(c_)


if __name__== "__main__":
	main()

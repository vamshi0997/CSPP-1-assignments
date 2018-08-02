'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    ''' start of main '''
    str_ = input()
    # the input string is in s
    # remove pass and start your code here
    le_ = len(str_)
    str1_ = ""
    max = ""
    for i in range(le_ -1):
        if str_[i] <= str_[i+1]:
            str1_ = str1_ + str_[i]
            if (i == le_-2):
                str1_ = str1_+str_[i+1]
        else:
            str1_ = str1_ + str_[i]
            if len(str1_) > len(max):
                max = str1_
            str1_ = ""
    if len(str_) == 1:
    	str1_ = str_

    if len(str1_) > len(max):
        print(str1_)
    else:
        print(max)

if __name__== "__main__":
	main()

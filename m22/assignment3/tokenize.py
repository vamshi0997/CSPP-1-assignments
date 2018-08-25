'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def cleanup(word):
    '''cleaning up'''
    words = []
    list1 = []
    regex = re.compile('[^a-z],[^A-Z],[^0-9]')
    for w in word:
        n = w.strip('"').strip('.').strip(';').strip(',').strip('"')
        words.append((regex.sub("", n)))
    return words

def tokenize(string):
    ''' make a dictionary'''
    dictionary = dict()
    word = cleanup(string)
    for i in word:
    	if i in word:
    		dictionary[i] = word.count(i)
    return dictionary
            
def main():
    ''' num: given input'''
    num = int(input())
    list1 = []
    for i in range(num):
    	list1 = list1 + input().split()
    print(tokenize(list1))
    

if __name__ == '__main__':
    main()

'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    text1 = cleanup(dict1)
    text2 = cleanup(dict2)

    stopwords = load_stopwords("stopwords.txt")
    text1 = remove_stopwords(text1, stopwords)
    text2 = remove_stopwords(text2, stopwords)
    diction = dict()
    diction = create_dictionary(text1, text2, diction)
    return compute(diction)

def remove_stopwords(word, stopwords):
    words1 = [i for i in word if i not in stopwords and len(i) > 0]
    return words1

def cleanup(doc):
    word = doc.lower()
    word = word.split(" ")
    words1 = []
    words = []
    for wor in word:
        words.append(wor.strip())
    regex = re.compile('[^a-z]')
    for wor in words:
            words1.append((regex.sub("", wor)))
    return words1

def create_dictionary(word, word1, diction):
    for i in word:
        list1 = []
        list1.append(word.count(i))
        if i not in word1:
            list1.append(0)
            diction[i] = list1
        else:
            list1.append(word1.count(i))
            diction[i] = list1
    for i in word1:
        if i not in diction:
            diction[i] = [0, word1.count(i)]
    return diction

def compute(diction):
    ''
    compute the diction.
    ''
    numerator = sum([i[0]*i[1] for i in diction.values()])
    denominator1 = math.sqrt(sum([i[0]**2 for i in diction.values()]))
    denominator2 = math.sqrt(sum([i[1]**2 for i in diction.values()]))
    return(numerator/(denominator1*denominator2))

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as file:
        for line in file:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

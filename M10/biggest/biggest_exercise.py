'''#Exercise : Biggest Exercise
#Write a procedure, called biggest,
#which returns the key corresponding to the entry with
#the largest number of values associated with it.
#If there is more than one such entry, return any one of the matching keys.'''


def biggest(adict):
    '''
    adict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    temp = 0
    max1 = 0
    key1 = ""
    for ke_, var in adict.items():
        temp = len(var)
        if temp > max1:
            max1 = temp
            key1 = ke_
        elif temp == max1:
            key1 = key1+","+ke_
    return key1

def main():
    ''' enter the length of dictionary'''
    num = input()
    adict = {}
    for i in range(int(num)):
        se_ = input()
        le_ = se_.split()
        if le_[0][0] not in adict:
            adict[le_[0][0]] = [le_[1]]
        else:
            adict[le_[0][0]].append(le_[1])
    print(biggest(adict))

if __name__ == "__main__":
    main()

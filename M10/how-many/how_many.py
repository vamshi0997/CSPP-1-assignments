'''#Exercise : how many
# write a procedure, called how_many,
#which returns the sum of the number of values associated with a dictionary.'''


def how_many(dict_):
    '''
    dict_: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum1 = 0
    for k1_, v1_ in dict_.items():
        sum1 += (len(v1_))
    return sum1

def main():
    '''
    n: length of dictionary
    '''
    n1_ = input("enter the length of dictionary:")
    dict_ = {}
    for i in range(int(n1_)):
        s1_ = input()
        l1_ = s1_.split()
        if l1_[0][0] not in dict_:
            dict_[l1_[0][0]] = [l1_[1]]
        else:
            dict_[l1_[0][0]].append(l1_[1])
    print("Total no of values:", how_many(dict_))



if __name__ == "__main__":
    main()

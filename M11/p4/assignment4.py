'''#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.'''

def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    count1 = 0
    for i in hand.values():
        count1 = count1 + i
    return count1

def main():
    '''
    n: length of the dictionary
    '''
    num1 = input()
    adict = {}
    for i in range(int(num1)):
        data = input()
        list1 = data.split()
        adict[list1[0]] = int(list1[1])
    print(calculatehandlen(adict))

if __name__ == "__main__":
    main()

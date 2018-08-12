'''#Exercise: Assignment-2
#Implement the updateHand function.
Make sure this function has no side effects:
i.e., it must not mutate the hand passed in.
Before pasting your function definition here,
be sureyou've passed the appropriate tests in test_ps4a.py.'''


def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    adic = {}
    for i in hand:
        if i in word:
            adic[i] = hand[i] - word.count(i)
        else:
            adic[i] = hand[i]
    return adic

def main():
    ''' inside main function'''
    num1 = input()
    adict = {}
    for i in range(int(num1)):
        i = i + 1
        data = input()
        len1 = data.split()
        adict[len1[0]] = int(len1[1])
    data1 = input()
    print(updatehand(adict, data1))

if __name__ == "__main__":
    main()

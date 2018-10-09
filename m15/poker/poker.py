'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
'''

def hand_to_nos(hand):
    """ returns list of numbers from the string hand"""
    nos_ = []
    fc_ = ('T', 'J', 'Q', 'K', 'A')
    num_ = None
    for i in hand:
        try:
            num_ = int(i[0])
        except ValueError:
            num_ = 10 + fc_.index(i[0])
        finally:
            nos_.append(num_)
    return nos_



def is_fourofakind(hand):
    ''' returns true if hand is 4 of a kind else false'''
    return len(set(i[0] for i in hand)) == 2

def is_threeofakind(hand):
    ''' returns true if hand is 3 of a kind else false'''
    hand_copy = [i[0] for i in hand]
    return any([True if hand_copy.count(i) == 3 else False for i in hand_copy])


def is_onepair(hand):
    ''' returns true if hand is one pair else false'''
    hand_copy = [i[0] for i in hand]
    return any([True if hand_copy.count(i) == 2 else False for i in hand_copy])

def is_twopair(hand):
    """ returns true if the hand is two pair else false"""
    return len(set(i[0] for i in hand)) == 3



def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    nos_ = hand_to_nos(hand)
    if all([True if i[0] in 'A234' else False for i in hand]):
        return True
    if len(set(nos_)) == 5 and max(nos_) - min(nos_) == 4:
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    tmp = hand[0][-1]
    for i in hand:
        if tmp != i[-1]:
            return False
    return True

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand

    funcs = ['', is_onepair, is_twopair, is_threeofakind, is_straight, is_flush, \
            [is_threeofakind, is_onepair], is_fourofakind, [is_straight, is_flush]]

    for i in range(8, 0, -1):
        if not isinstance(funcs[i], list):
            if funcs[i](hand):
                return i
        else:
            if funcs[i][0](hand) and funcs[i][1](hand):
                return i
    return 0

def get_highcardvalue(hand, hand_rank_):
    """ returns the kicker based on its rank"""
    nos_ = hand_to_nos(hand)
    if hand_rank_ in (0, 8):
        return max(nos_)
    max_freq = 0
    max_freq_element = 0
    for i in nos_:
        tmp_ = nos_.count(i)
        if tmp_ > max_freq:
            max_freq = tmp_
            max_freq_element = i
    return max_freq_element

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.
        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation
        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    #hands.reverse()
    #return max(hands, key=hand_rank)
    ranks_ = list(map(hand_rank, hands))
    max_rank = max(ranks_)
    if ranks_.count(max_rank) == 1:
        return hands[ranks_.index(max_rank)]
    high_card = 0
    high_card_index = 0
    for i, val in enumerate(ranks_):
        if val == max_rank:
            value_ = get_highcardvalue(hands[i], max_rank)
            #print(value_)
            if value_ > high_card:
                high_card = value_
                high_card_index = i
    return hands[high_card_index]

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
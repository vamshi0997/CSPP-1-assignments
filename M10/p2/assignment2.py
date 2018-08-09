from assignment import get_guessed_word
from assignment1 import get_available_letters
import random
import string
'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretword
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
'''
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secretword):
    '''
    secretword: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secretword contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", (secretword), "letters long.")
    print("------------------------------------------------")
    guess = 10
    set1 = ""
    res = ""
    print("you have", guess, "guesses left")
    alp = string.ascii_lowercase
    print("Available letters:", alp)
    while 1:
        var = input("Please guess a letter:")
        set1 = set1 + var
        if guess <= 1:
            print("Sorry, you ran out of guesses. The word was else.")
            break
        elif var in res:
            print("Oops! You've already guessed that letter:", get_guessed_word(secretword, res))
        elif secretword == get_guessed_word(secretword, set1):
            print("Congratulations, you won!")
            break
        elif var in alp:
            print("Good guess:", get_guessed_word(secretword, set1))
            guess = guess - 1
        elif var not in alp:
            print("Oops! That letter is not in my word:", get_guessed_word(secretword, set1))
            guess = guess - 1
        res = res + var
        print(set1)
        print("------------------------------------------------")
        print("you have", guess, "guesses left")
        print("Available letters:", get_available_letters(set1))


def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretword while you're testing)
    '''
    secretword = chooseword(wordlist).lower()
    hangman(secretword)

if __name__ == "__main__":
    main()

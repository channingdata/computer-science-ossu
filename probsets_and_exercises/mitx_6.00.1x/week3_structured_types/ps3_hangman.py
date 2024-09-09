# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import sys

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

def chooseWord(wordlist):
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter + ' '
        else:
            word += '_ '
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = []
    for letter in all_letters:
        if letter not in lettersGuessed:
            available_letters.append(letter)
    return ''.join(available_letters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print(
        f"\n\nGame Starts\n\n"
        f"This is a {len(secretWord)}-letter word.\n"
    )

    round = 1
    lettersGuessed = []
    mistakesMade = 0
    availableLetters = getAvailableLetters(lettersGuessed)

    while mistakesMade < 9:
        guessLetter = input(f"Please guess a letter (Round {round}. Mistakes {mistakesMade}): ")
        if guessLetter in lettersGuessed:
            print("The input letter is already in the correctly guessed letters")
        else:
            if guessLetter in secretWord:
                lettersGuessed.append(guessLetter)
                if isWordGuessed(secretWord, lettersGuessed):
                    print(
                        f"You won the game\n"
                        f"The word is {secretWord}\n"
                        f"Your guess: {getGuessedWord(secretWord, lettersGuessed)}"
                    )
                    sys.exit()
            else:
                mistakesMade += 1

        round += 1

        print(
            f"Currently guessed word: {getGuessedWord(secretWord, lettersGuessed)}\n"
            f"Available letters: {getAvailableLetters(lettersGuessed)}\n"
        )
    
    print(
        f"You lost the game\n"
        f"The word is {secretWord}\n"
        f"Your guess: {getGuessedWord(secretWord, lettersGuessed)}"
    )


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

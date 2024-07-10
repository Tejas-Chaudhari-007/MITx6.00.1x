# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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

def isWordGuessed(secretWord: str, lettersGuessed: list[str]) -> bool:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    return all(list(map(lambda x: x in lettersGuessed, list(secretWord))))

def getGuessedWord(secretWord: str, lettersGuessed: list[str]) -> str:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    return ''.join(map(lambda x: x if x in lettersGuessed else '_ ', list(secretWord)))

def getAvailableLetters(lettersGuessed: list[str]) -> str:
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    return ''.join(map(lambda x: '' if x in lettersGuessed else x, list(string.ascii_lowercase)))

def hangman(secretWord: str):
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

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    print('-' * 13)

    lettersGuessed = []
    numGuesses = 8

    while numGuesses > 0:
        print(f'You have {numGuesses} guesses left.')

        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:', availableLetters)

        guess = input('Please guess a letter: ').lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            numGuesses -= 1

        print('-' * 13)

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        elif numGuesses == 0:
            print(f'Sorry, you ran out of guesses. The word was {secretWord}')
        else:
            continue



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

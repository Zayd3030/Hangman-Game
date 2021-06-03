#########################################################################################
# Hangman Game Project (Python 3.7)
#########################################################################################

#import

import random

# variables

allowed_errors = 6
guesses = []
correctLetters = ''
done = False

# functions

def print_greeting():
    print("Lets Play Hangman! ")

def get_words():
    return  ["Table", "Computer", "Python", "Science", "Football", "Netflix", "Bottle", "Music", "America", "Britain", "Youtube", "Google"]

def get_word(words):
    return random.choice(words).lower()

def print_hangman():
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print(" * ", end=" ")
    print("")
    print(f"You Have {allowed_errors} Guesses Left")

def get_guess():
    return input("Your Next Guess: ").lower()

def check_guess(guess):
    if guess not in guesses:
        guesses.append(guess)
    else:
        print (f"Already guessed {guess}")
        return True
    if guess not in word: 
        return False
    else:
        return True

def has_won(correctLetters):
    foundAllLetters = False
    for guess in guesses:
        if guess in word:
            correctLetters = correctLetters + guess
            # Check if the player has won.
            foundAllLetters = True
            for i in range(len(word)):
                if word[i] not in correctLetters:
                    foundAllLetters = False
                    break
    
    if foundAllLetters:
        return True
    else :
        return False

def no_more_guesses(allowed_errors):
    if allowed_errors > 0:
        return False
    else:
        return True

#########################################################################################
# main program
#########################################################################################

words = get_words()
word = get_word(words)

print_greeting()

# Adds the number of * for each letter
while not done:

    print_hangman()
    
    guess = get_guess()
    
    if not check_guess(guess):
        allowed_errors -= 1

    if has_won(correctLetters):
        print(f"You found the word! The word was {word}!")
        done = True
    
    if no_more_guesses(allowed_errors):
        print(f"Game Over :( The word was {word}!")
        done = True

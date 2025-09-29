#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter.lower() in word.lower()

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if spot < 0 or spot >= len(word):
        return False
    return letter.lower() == word[spot].lower()

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for i, letter in enumerate(myGuess):
        if inSpot(letter, word, i):
            result += letter.upper()
        elif inWord(letter, word):
            result += letter.lower()
        else:
            result += "*"
    return result


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    wordFile.close()
    # Filter to ensure only 5-letter words
    wordList = [word.strip() for word in wordList if word.strip() and len(word.strip()) == 5]
    todayWord = random.choice(wordList).lower()
    
    print("Welcome to the Word Game!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print("Feedback: UPPERCASE = correct position, lowercase = wrong position, * = not in word")
    print()

    #User should get 6 guesses to guess
    guesses = 0
    max_guesses = 6
    won = False

    while guesses < max_guesses and not won:
        #Ask user for their guess
        guess = input(f"Guess {guesses + 1}/{max_guesses}: ").strip()
        
        # Validate input
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        if not guess.isalpha():
            print("Please enter letters only.")
            continue
            
        guesses += 1
        
        #Give feedback using on their word:
        feedback = rateGuess(guess, todayWord)
        print(f"Feedback: {feedback}")
        
        # Check if won
        if guess.lower() == todayWord.lower():
            won = True
            print(f"Congratulations! You guessed the word '{todayWord}' in {guesses} attempts!")
        else:
            print()
    
    if not won:
        print(f"Game over! The word was '{todayWord}'.")


if __name__ == '__main__':
  main()

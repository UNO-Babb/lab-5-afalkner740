[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20762298)
# Lab 5

## Cryptography
As long as people have had secrets, we have devised ways to write them in a way that others cannot read. These secrets are shared in times of war, during attempts to overthrow a government, and today as a routine part of internet communication. Communicating secrets where others may be listening is an age old challenge, made more difficult by the code-cracking abilities of modern computers.

### Mary Queen of Scots
In the late 1500s, Mary Tudor was beheaded by her cousin, Queen Elizabeth of England. Her plot to take the British crown had been uncovered.

Mary believed her messages were secret because of the complex code she used to communicate with her co-conspirators.

![Mary Queen of Scots](MaryQoS.png)
### Julius Caesar
The Caesar Cipher works by shifting each letter in a message by a set amount up the alphabet. For example, in a Caesar Cipher with a key (shift) of 3, A -> D and so on, looping around the end so Z -> C.

Take the **CaesarCipher.py** file and examine:
- how it takes input in the ***main()*** function
- how it sends that message to the ***encode()*** function
- how the letter position is determined
- how each letter examined one at a time
- how the key value is added
  - What happens if the letter + key value is outside the alphabet range?
- What happens if the given letter is not in the alphabet?

### Letter Frequency
In an alphabetic substitution cipher, each letter is paired with another letter to form the key. Unlike the Caesar Cipher, there are more possible ways to swap the letters (26! instead of 26). To break this type of cipher, we will analyze the frequency of each letter to see if we can find a relationship to the known frequency of letters in the English language.

![English Letter Frequency](ENG_FRQ.png)

#### LetterFrequency.py
- loop through each letter
- Find the position in the alphabet
- Increase the frequency at that position.
  - If position was 5, then frequencies[5] = frequencies[5] + 1

After you have counted how many of each letter are in your message, we will save this info to a .csv file.
Open the file in Excel and create a chart using the data. Save the file with the chart and make sure that it is added to your repl.it files.

![Frequency Chart](FrequencyGraph.png)

### Word Game (not a NYT property)
We will be re-creating a (currently) popular word game where a user guesses 5-letter words and gets feedback on their guess.

#### WordGame.py
You will finish the word game in a few important ways. There are three helper functions we will look at completing.
#### inWord(letter, word)
This function returns True or False depending on the state of the given letter being anywhere in the word.

#### inSpot(letter, word, spot)
This function returns True or False if the letter is in the word at the given spot.

#### rateGuess(myGuess, word)
Rates your guess and returns a word with the following features.
- Capital letter if the letter is in the right spot
- Lower case letter if the letter is in the word but in the wrong spot
- * if the letter is not in the word at all

#### main()
Your main function should randomly select a word from the list of all possible words.
You will give the user 6 tries to get the correct word
If they get it early, end the loop and congratulate.
Use the helper methods to determine if the user got any letters correct.

---
## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
- Add a commit message
- Commit to GitHub
- Sync work with Repo
- Submit your repo link to Canvas

### Additional Resources
- [Cracking Codes with Python](http://inventwithpython.com/cracking/)
- [Caesar Cipher](http://practicalcryptography.com/ciphers/caesar-cipher/)
- [NSA Crypto Challenge](https://cryptochallenge.io/)
- [Enigma Rotor Details](https://en.wikipedia.org/wiki/Enigma_rotor_details)

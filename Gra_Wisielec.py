    # Hangman Project
import os
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

wordList = ["motor", "bartek", "władca"]

wordToGuess = random.choice(wordList)
wordToGuess = list(wordToGuess)
lenWordToGuess = len(wordToGuess)

display = []
for letter in range(lenWordToGuess):
    display += "_"
print(' '.join(display))

endOfGame = False
lives = 6
# mistake = False

while not endOfGame:
    guess = (input("Guess a letter: ")).lower()
    
    clear = lambda: os.system('cls')
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    for letter in range(lenWordToGuess):
        if wordToGuess[letter] == guess:
            display[letter] = guess
        #     mistake = True
        # elif (mistake == False) and (letter + 1 == lenWordToGuess):
        #     print(stages[(len(stages)-1) - lives])
        #     lives -= 1
    if guess not in wordToGuess:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            endOfGame = True
            print("You lose.")

            
    # mistake = False
    print(' '.join(display))

# if "something" in "list": do something

    if "_" not in display:
        endOfGame = True
        print("You win!")
    # elif lives == -1:
    #     print("You lost!")
    #     break
    print(stages[(len(stages)-1) - lives])
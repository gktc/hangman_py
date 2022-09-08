from hangman_art import stages, logo
import words
import os

lives = 6
word = words.getWord()
letter_bag = ['_' for i in range(len(word))]
won = False
guessed_word = []

print(logo)
print(word)
print(letter_bag)

while lives > 0 and won == False:
    guess = input("Guess the letter : ").lower()
    os.system('clear')
  
    if guess in guessed_word:
        print(f"You have already guessed the letter {guess}. Try again!!!")
    else:
        guessed_word.append(guess)

        if guess not in word:
            print(
                f"You have guessed the letter {guess}. It's not in this word. You lose a life."
            )
            lives -= 1
        else:
            for i in range(len(word)):
                if (word[i] == guess):
                    letter_bag[i] = guess

            if ('_' not in letter_bag):
                won = True
                print("You won")
                print(stages[lives])
                print(letter_bag)

        print(stages[lives])
        print(letter_bag)
if (lives <= 0):
  os.system('clear')
  print("You Lost")
  print(stages[lives])
  print(letter_bag)
  print(f"The word was {word.upper()}")
  
  

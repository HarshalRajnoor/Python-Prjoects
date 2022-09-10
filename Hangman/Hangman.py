import random

from hangman_art import stages, logo

from hangman_words import word_list

# Lives
lives = 6

# Chosen random word
chosenWord = random.choice(word_list)

# printing hangman logo
print(logo)


# for debugging
print(f'The solution is {chosenWord}.')

# Displays blanks
display = []
for _ in chosenWord:
    display += "_"

# print(display)
print(f"{' '.join(display)}")

endOfGame = False

while not endOfGame:
  
    # User guess
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Checking if the user's guess matches the chosen random word
    for i in range(len(chosenWord)):
        letter = chosenWord[i]

        if letter == guess:
            display[i] = letter

    # if the user guess does not matches any word in the chosen word
    if guess not in chosenWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfGame = True

    # joining elements of the list to form a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfGame = True
        print("You Win!")

    # Printing hangman figures
    print(stages[lives])

    if lives == 0:
        print("You Lost!")

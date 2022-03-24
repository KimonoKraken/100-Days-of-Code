import random
from hangman_art import stages, logo
from hangman_words import word_list
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
    
print(logo)
game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("\nGuess a letter: ").lower()

    #Use the clear function imported from os
    clearConsole()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"\nYou lose. The word was '{chosen_word}'")
    
    if not "_" in display:
        game_is_finished = True
        print("\nYou win.")

    print(stages[lives])

import random

list_words = ["python","paris","skills","love","mother", "nextjs", "hope", "laptop", "database", "home", "computer", "engineer", "code", "alpha", "vscode"]

# select a random word from the list_words list
def random_word():
    return random.choice(list_words)

# function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# function to play the Hangman game
def play_hangman():
    word = random_word()  
    guessed_letters = []  
    incorrect_guesses = 0  
    max_incorrect_guesses = 6  

    print("Welcome to the Hangman game!")
    print("You have", max_incorrect_guesses, "incorrect answers allowed")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print("Guessed letters:", guessed_letters)
        print(f"Remaining incorrect answers: {max_incorrect_guesses - incorrect_guesses}")
        
        # ask the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # check if the input is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue
        
        # add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # check if the letter is in the word
        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}' correctly!")
            break
    else:
        print(f"\nGame over! The word was '{word}'. Better luck next time!")

# start the game
play_hangman()
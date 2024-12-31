import random
import tkinter as tk
from tkinter import messagebox

list_words = ["python", "paris", "skills", "love", "mother", "nextjs", "hope", "laptop", "database", "home", "computer", "engineer", "code", "alpha", "vscode"]

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

# initialize game state
word = random_word()
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

# function to handle letter guessing
def guess_letter():
    global incorrect_guesses
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a single valid letter.")
        return

    if letter in guessed_letters:
        messagebox.showwarning("Duplicate Guess", f"You already guessed '{letter}'.")
        return

    guessed_letters.append(letter)
    if letter in word:
        update_display()
        if all(l in guessed_letters for l in word):
            messagebox.showinfo("Congratulations!", f"You guessed the word '{word}' correctly!")
            reset_game()
    else:
        global incorrect_guesses
        incorrect_guesses += 1
        update_display()
        if incorrect_guesses >= max_incorrect_guesses:
            messagebox.showerror("Game Over", f"You lost! The word was '{word}'.")
            reset_game()

# function to update the word display and remaining attempts
def update_display():
    word_label.config(text=display_word(word, guessed_letters))
    guessed_label.config(text=f"Guessed Letters: {', '.join(guessed_letters)}")
    attempts_label.config(text=f"Remaining Attempts: {max_incorrect_guesses - incorrect_guesses}")

# function to reset the game
def reset_game():
    global word, guessed_letters, incorrect_guesses
    word = random_word()
    guessed_letters = []
    incorrect_guesses = 0
    update_display()

# create the main tkinter window
root = tk.Tk()
root.title("Hangman Game")

# create and place widgets
word_label = tk.Label(root, text=display_word(word, guessed_letters), font=("Helvetica", 24))
word_label.pack(pady=20)

guessed_label = tk.Label(root, text="Guessed Letters: ", font=("Helvetica", 14))
guessed_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Remaining Attempts: {max_incorrect_guesses}", font=("Helvetica", 14))
attempts_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 16))
guess_button.pack(pady=20)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 16))
reset_button.pack(pady=10)

# start the tkinter main loop
update_display()
root.mainloop()

import tkinter as tk
import random

# Function to handle letter guess
def guess_letter():
    global remaining_attempts, guessed_letters, word_state, hangman_figure
    letter = letter_entry.get().lower()
    
    if letter in guessed_letters:
        result_label.config(text="You've already guessed that letter.")
    else:
        guessed_letters.add(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_state[i] = letter
            if "_" not in word_state:
                result_label.config(text="Congratulations! You've guessed the word.")
                remaining_attempts = 0
        else:
            remaining_attempts -= 1
            hangman_figure.config(text=hangman_figures[6 - remaining_attempts])
            if remaining_attempts == 0:
                result_label.config(text=f"Game over! The word was '{word}'.")

    word_label.config(text=" ".join(word_state))
    letter_entry.delete(0, tk.END)

# Function to start a new game
def new_game():
    global word, word_state, remaining_attempts, guessed_letters
    word = random.choice(word_list).lower()
    word_state = ["_" for _ in word]
    remaining_attempts = 6
    guessed_letters = set()
    word_label.config(text=" ".join(word_state))
    hangman_figure.config(text="")
    result_label.config(text="")

# Setting up the main window
root = tk.Tk()
root.title("Hangman Game")

# Word list
word_list = ["apple", "banana", "orange", "grape", "peach", "watermelon", "kiwi"]

# Global variables
word = ""
word_state = []
remaining_attempts = 6
guessed_letters = set()

# Hangman figures
hangman_figures = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
]

# Word label
word_label = tk.Label(root, text="", font=("Arial", 18))
word_label.pack(pady=10)

# Hangman figure label
hangman_figure = tk.Label(root, text="", font=("Courier New", 14))
hangman_figure.pack()

# Letter entry
letter_entry = tk.Entry(root, font=("Arial", 14), width=5)
letter_entry.pack(pady=5)

# Guess button
guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# New game button
new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack()

# Start a new game initially
new_game()

# Running the main loop
root.mainloop()

import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password(length, include_uppercase, include_digits, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the button click
def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        include_uppercase = uppercase_var.get()
        include_digits = digits_var.get()
        include_symbols = symbols_var.get()
        password = generate_password(length, include_uppercase, include_digits, include_symbols)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Creating the main window
root = tk.Tk()
root.title("Password Generator")

# Creating and placing widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for additional options
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Running the main loop
root.mainloop()

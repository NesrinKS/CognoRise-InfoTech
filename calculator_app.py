import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the entry box
def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(symbol))

# Function to clear the entry box
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        current_text = entry.get()
        result = eval(current_text)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear_entry()

# Creating the main window
root = tk.Tk()
root.title("Calculator")

# Creating an entry widget for displaying expressions and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Defining button texts and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Creating and placing buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Running the main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown
def start_countdown():
    global remaining_time
    try:
        duration = int(duration_entry.get())
        remaining_time = duration
        update_label()
        countdown()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid duration (in seconds)")

# Function to update the label with remaining time
def update_label():
    timer_label.config(text=f"Time remaining: {remaining_time} seconds")
    if remaining_time > 0:
        root.after(1000, update_label)

# Function to countdown
def countdown():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        root.after(1000, countdown)
    else:
        messagebox.showinfo("Time's up!", "The countdown has finished.")

# Setting up the main window
root = tk.Tk()
root.title("Countdown Timer")

# Label and entry for duration
duration_label = tk.Label(root, text="Enter duration (seconds):")
duration_label.pack(pady=5)
duration_entry = tk.Entry(root)
duration_entry.pack(pady=5)

# Button to start countdown
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=5)

# Label to display remaining time
timer_label = tk.Label(root, text="Time remaining: 0 seconds")
timer_label.pack(pady=5)

# Running the main loop
root.mainloop()

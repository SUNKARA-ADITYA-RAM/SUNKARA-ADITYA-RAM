import tkinter as tk
import random
from tkinter import messagebox

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            messagebox.showinfo("Result", "Too low!")
        elif guess > number:
            messagebox.showinfo("Result", "Too high!")
        elif guess == number:
            messagebox.showinfo("Result", "Congratulations! You guessed it!")
            restart_game()
    except:
        messagebox.showwarning("Error", "Enter a valid number.")

def restart_game():
    global number
    number = random.randint(1, 100)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x200")

number = random.randint(1, 100)

tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)
tk.Button(root, text="Submit", font=("Arial", 14), command=check_guess).pack(pady=10)

root.mainloop()

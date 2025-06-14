import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.lower_bound = 1
        self.upper_bound = 100
        self.max_attempts = 7
        self.reset_game()

        self.label = tk.Label(root, text=f"Guess a number between {self.lower_bound} and {self.upper_bound}")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.status = tk.Label(root, text=f"Attempts left: {self.max_attempts}")
        self.status.pack()

    def reset_game(self):
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return

        if guess < self.lower_bound or guess > self.upper_bound:
            messagebox.showinfo("Out of Range", f"Guess must be between {self.lower_bound} and {self.upper_bound}")
            return

        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts

        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} tries!")
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Out of attempts! The number was {self.secret_number}.")
            self.reset_game()
        elif guess < self.secret_number:
            self.status.config(text=f"Too low! Attempts left: {attempts_left}")
        else:
            self.status.config(text=f"Too high! Attempts left: {attempts_left}")

        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

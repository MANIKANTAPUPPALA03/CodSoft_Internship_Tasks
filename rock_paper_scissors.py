import tkinter as tk
import random
from tkinter import messagebox


def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    Computer = random.choice(choices)

    if choice == Computer:
        result = "It's a tie!"
    elif (choice == "Rock" and Computer == "Scissors") or \
         (choice == "Paper" and Computer == "Rock") or \
         (choice == "Scissors" and Computer == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {Computer}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

rock = tk.Button(root, text="Rock", command=lambda: play("Rock"))
paper = tk.Button(root, text="Paper", command=lambda: play("Paper"))
scissors = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))

rock.pack(pady=10)
paper.pack(pady=10)
scissors.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

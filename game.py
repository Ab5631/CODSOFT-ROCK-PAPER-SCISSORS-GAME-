# ROCK,PAPER,SCISSORS GAME :

import random
import tkinter as tk

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])

    result_label.config(text=f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1

    score_label.config(text=f"Your Score: {user_score}\nComputer Score: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

title_label = tk.Label(root, text="Rock, Paper, Scissors")
title_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text="")
score_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

root.mainloop()

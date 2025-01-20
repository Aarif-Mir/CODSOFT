import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    """Randomly generates the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round(user_choice):
    """Handles a single round of the game."""
    global user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        result_text.set(f"You win!\nYou chose {user_choice}, computer chose {computer_choice}.")
    elif result == "computer":
        computer_score += 1
        result_text.set(f"You lose!\nYou chose {user_choice}, computer chose {computer_choice}.")
    else:
        result_text.set(f"It's a tie!\nYou both chose {computer_choice}.")

    update_score()

def update_score():
    """Updates the score labels."""
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    """Resets the game to the initial state."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("Welcome to Rock-Paper-Scissors! Make your choice.")
    update_score()

def end_game():
    """Ends the game and shows the final winner."""
    if user_score > computer_score:
        winner = "You win the game!"
    elif user_score < computer_score:
        winner = "Computer wins the game!"
    else:
        winner = "The game ends in a tie!"

    messagebox.showinfo("Game Over", f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}\n{winner}")
    reset_game()

def exit_game():
    """Exits the game with a confirmation."""
    if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
        root.destroy()

# Initialize scores
user_score = 0
computer_score = 0
# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="#f0f8ff")

# Create result text variable
result_text = tk.StringVar()
result_text.set("Welcome to Rock-Paper-Scissors! Make your choice.")

# Create widgets
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333")
result_label = tk.Label(root, textvariable=result_text, wraplength=500, font=("Arial", 12), bg="#f0f8ff", fg="#333")

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=("Arial", 12), bg="#f0f8ff", fg="#333")
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=("Arial", 12), bg="#f0f8ff", fg="#333")

rock_button = tk.Button(root, text="Rock", font=("Arial", 14), bg="#add8e6", command=lambda: play_round("rock"))
paper_button = tk.Button(root, text="Paper", font=("Arial", 14), bg="#98fb98", command=lambda: play_round("paper"))
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), bg="#ffb6c1", command=lambda: play_round("scissors"))

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), bg="#f0e68c", command=reset_game)
end_button = tk.Button(root, text="End Game", font=("Arial", 12), bg="#ffa07a", command=end_game)
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="#fa8072", command=exit_game)

# Layout the widgets using grid system
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Title and result labels centered
title_label.grid(row=0, column=0, pady=10, columnspan=3, sticky="nsew")
result_label.grid(row=1, column=0, pady=10, columnspan=3, sticky="nsew")

# Score labels centered
user_score_label.grid(row=2, column=0, pady=5, columnspan=3, sticky="nsew")
computer_score_label.grid(row=3, column=0, pady=5, columnspan=3, sticky="nsew")

# Buttons arranged in a row and centered
rock_button.grid(row=4, column=0, padx=15, pady=10, sticky="nsew")
paper_button.grid(row=4, column=1, padx=15, pady=10, sticky="nsew")
scissors_button.grid(row=4, column=2, padx=15, pady=10, sticky="nsew")

# Control buttons (Reset, End Game, Exit) arranged in a row and centered
reset_button.grid(row=5, column=0, padx=15, pady=10, sticky="nsew")
end_button.grid(row=5, column=1, padx=15, pady=10, sticky="nsew")
exit_button.grid(row=5, column=2, padx=15, pady=10, sticky="nsew")

# Start the Tkinter main loop
root.mainloop()




# Start the Tkinter main loop
root.mainloop()

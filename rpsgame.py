import tkinter as tk
from tkinter import ttk
import random

X = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0

def play(choice):
    global player_score, computer_score
    computer_choice = random.choice(X)

    if choice == computer_choice:
        result = "It's a draw!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "YAY!!! YOU WIN!!! :)"
        player_score += 1
    else:
        result = "OHH NOO! COMPUTER WINS :("
        computer_score += 1

    player_label.config(text=f"Your Choice: {choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {player_score} | Computer: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score, computer_score = 0, 0
    player_label.config(text="Your Choice: choose any 1 of the 3 choices")
    computer_label.config(text="Computer's Choice: choosing.....")
    result_label.config(text="Make your move!")
    score_label.config(text="Score → You: 0 | Computer: 0")

def on_enter(e):
    e.widget['style'] = "Hover.TButton"

def on_leave(e):
    e.widget['style'] = "TButton"

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.state("zoomed")   
root.config(bg="#222831")

# Modern style
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Calibri", 18, "bold"),
                padding=15,
                background="#00ADB5",
                foreground="white",
                borderwidth=0,
                focusthickness=3,
                focustcolor="none")
style.map("TButton",
          background=[("active", "#008C9E")])

style.configure("Hover.TButton",
                font=("Calibri", 18, "bold"),
                padding=15,
                background="#FF5722",
                foreground="white",
                borderwidth=0)

# Labels
title = tk.Label(root, text="Rock-Paper-Scissors", fg="white", bg="#222831",
                 font=("Calibri", 36, "bold"))
title.pack(pady=20)

player_label = tk.Label(root, text="Your Choice: choose any 1 of the 3 choices", fg="cyan", bg="#222831", font=("Calibri", 20))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer's Choice: choosing.....", fg="magenta", bg="#222831", font=("Calibri", 20))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", fg="yellow", bg="#222831", font=("Calibri", 24, "bold"))
result_label.pack(pady=15)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", fg="orange", bg="#222831", font=("Calibri", 20))
score_label.pack(pady=5)

# Button frame
btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack(pady=40)

rock_btn = ttk.Button(btn_frame, text="Rock", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=20)
rock_btn.bind("<Enter>", on_enter)
rock_btn.bind("<Leave>", on_leave)

paper_btn = ttk.Button(btn_frame, text="Paper", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=20)
paper_btn.bind("<Enter>", on_enter)
paper_btn.bind("<Leave>", on_leave)

scissors_btn = ttk.Button(btn_frame, text="Scissors", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=20)
scissors_btn.bind("<Enter>", on_enter)
scissors_btn.bind("<Leave>", on_leave)

reset_btn = ttk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=20)
reset_btn.bind("<Enter>", on_enter)
reset_btn.bind("<Leave>", on_leave)

root.mainloop()

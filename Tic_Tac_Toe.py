import tkinter as tk
from tkinter import messagebox

# Create the main window with black background
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x430")
root.config(bg="black")
root.resizable(False, False)

# Variables for the game state
current_p = "X"
board = [" " for _ in range(9)]

# Function to check for a win or a draw
def check_winner():
    # Winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    
    # Check for winner
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    
    # Check for draw
    if " " not in board:
        return "Draw"
    
    return None

# Function to handle button click
def b_click(index):
    global current_p

    if board[index] == " ":
        # Update board and button text
        board[index] = current_p
        buttons[index].config(text=current_p, state="disabled", disabledforeground="#41cc16")
        
        # Check for winner
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        else:
            # Switch player
            current_p = "O" if current_p == "X" else "X"
            update_turn_label()

# Function to reset the board
def reset_board():
    global board, current_p
    board = [" " for _ in range(9)]
    current_p = "X"
    update_turn_label()
    for button in buttons:
        button.config(text=" ", state="normal", bg="#c983b9")

# Function to update the turn label
def update_turn_label():
    turn_label.config(text=f"Player {current_p}'s Turn")

# Title Label
title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#a88ad4", fg="#ccc916")
title_label.pack(pady=20)

# Turn Label
turn_label = tk.Label(root, text=f"Player {current_p}'s Turn", font=("Arial", 14), bg="#a88ad4", fg="#555")
turn_label.pack()


frame = tk.Frame(root, bg="#c99983")
frame.pack(pady=10)
buttons = []
for i in range(9):
    button = tk.Button(
        frame, 
        text=" ", 
        font=("Arial", 20, "bold"), 
        width=5, 
        height=2, 
        command=lambda i=i: b_click(i),
        bg="#c983b9", 
        activebackground="#adf0c3"
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)


reset_button = tk.Button(
    root, 
    text="Reset Game", 
    font=("Arial", 12, "bold"), 
    command=reset_board, 
    padx=20, 
    pady=10
)
reset_button.pack(pady=20)


root.mainloop()
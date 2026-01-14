import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x400")
        self.root.config(bg="#2c3e50")

        self.user_score = 0
        self.comp_score = 0
        self.choices = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

        # Score Board
        self.score_label = tk.Label(root, text="User: 0  |  Computer: 0", font=("Helvetica", 14, "bold"), fg="white", bg="#2c3e50")
        self.score_label.pack(pady=20)

        # Result Display
        self.result_label = tk.Label(root, text="Choose your weapon!", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
        self.result_label.pack(pady=10)

        # Battle Arena
        self.arena_frame = tk.Frame(root, bg="#2c3e50")
        self.arena_frame.pack(pady=20)
        self.user_choice_label = tk.Label(self.arena_frame, text="❔", font=("Arial", 40), bg="#2c3e50", fg="white")
        self.user_choice_label.grid(row=0, column=0, padx=30)
        tk.Label(self.arena_frame, text="VS", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#e74c3c").grid(row=0, column=1)
        self.comp_choice_label = tk.Label(self.arena_frame, text="❔", font=("Arial", 40), bg="#2c3e50", fg="white")
        self.comp_choice_label.grid(row=0, column=2, padx=30)

        # Buttons
        btn_frame = tk.Frame(root, bg="#2c3e50")
        btn_frame.pack(pady=20)
        
        for choice in self.choices:
            tk.Button(btn_frame, text=f"{choice} {self.choices[choice]}", width=10, 
                      command=lambda c=choice: self.play(c)).pack(side=tk.LEFT, padx=5)

        # Reset Button
        tk.Button(root, text="Reset Score", command=self.reset_game, bg="#e74c3c", fg="white").pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(list(self.choices.keys()))
        
        # Update Icons
        self.user_choice_label.config(text=self.choices[user_choice])
        self.comp_choice_label.config(text=self.choices[comp_choice])

        # Logic
        if user_choice == comp_choice:
            result = "It's a Tie!"
            color = "yellow"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
            color = "#2ecc71" # Green
        else:
            result = "Computer Wins!"
            self.comp_score += 1
            color = "#e74c3c" # Red

        self.result_label.config(text=result, fg=color)
        self.score_label.config(text=f"User: {self.user_score}  |  Computer: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="User: 0  |  Computer: 0")
        self.result_label.config(text="Game Reset", fg="white")
        self.user_choice_label.config(text="❔")
        self.comp_choice_label.config(text="❔")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
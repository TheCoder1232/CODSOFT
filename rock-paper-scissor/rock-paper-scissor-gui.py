import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x200")
        self.root.resizable(0,0)
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice):
        computer_choice = self.get_computer_choice()

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "Player wins!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_game(self, user_choice):
        result = self.determine_winner(user_choice)
        self.computer_label.config(text=f"Computer chooses {self.get_computer_choice()}")
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")

    def run_game(self):

        instruction_label = tk.Label(self.root, text="Choose your move:")
        instruction_label.grid(row=0, column=0)

        button_frame = tk.Frame(self.root, height=80).grid(row=1, column=0)

        rock_button = tk.Button(button_frame, text="Rock", width=10, background="#21a366", command=lambda: self.play_game('rock'))
        rock_button.place(x=40, y=50)

        paper_button = tk.Button(button_frame, text="Paper", width=10, background="#21a366", command=lambda: self.play_game('paper'))
        paper_button.place(x=160, y=50)

        scissors_button = tk.Button(button_frame, text="Scissors", width=10, background="#21a366", command=lambda: self.play_game('scissors'))
        scissors_button.place(x=280, y=50)

        self.computer_label = tk.Label(self.root, text="")
        self.computer_label.grid(row=2, column=1, ipadx=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=1)

        self.score_label = tk.Label(self.root, text="Score: You 0 - Computer 0")
        self.score_label.grid(row=4, column=1)

        self.root.mainloop()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.run_game()

import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie!"
        elif (self.choices[user_choice-1] == 'rock' and computer_choice == 'scissors') or \
             (self.choices[user_choice-1] == 'paper' and computer_choice == 'rock') or \
             (self.choices[user_choice-1] == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "Player wins!"
        else:
            self.computer_score += 1
            return "Computer wins!"

def main():
    game = RockPaperScissors()
    print("Rock Paper Scissors")

    while True:
        print("\nCurrent Score:")
        print(f"You: {game.user_score}  Computer: {game.computer_score}")

        user_choice = input("Enter your choice (1 - rock, 2 - paper, or 3 - scissors) or 'q' to quit: ")

        if user_choice == 'q':
            print("Thanks for playing!")
            break

        if int(user_choice) not in (1, 2, 3):
            print("Invalid choice.")
            continue

        computer_choice = game.get_computer_choice()
        print(f"Computer chooses {computer_choice}")

        result = game.determine_winner(int(user_choice), computer_choice)
        print(result)

if __name__ == "__main__":
    main()

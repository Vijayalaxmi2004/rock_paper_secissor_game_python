import random
options=["Rock","paper","scissors"]
computer_option=random.choice(options)
user_choice=input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    print(f"Computer chose: {computer_option}")
    if user_choice==computer_option.lower():
        print("It's a tie!")
    elif user_choice=="rock" and computer_option=="scissors":
        print("You are the winner!")
    elif user_choice=="paper" and computer_option=="rock":
        print("You are the winner!")
    elif user_choice=="scissors" and computer_option=="paper":
        print("You are the winner!")
    else:
        print("You are the loser!")
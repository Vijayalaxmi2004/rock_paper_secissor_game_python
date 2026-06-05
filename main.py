import random
options=["Rock","paper","scissors"]
computer_choice=random.choice(options)
user_choice=input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    print(f"Computer chose: {computer_choice}")
    if user_choice==computer_choice.lower():
        print("tie")
    elif user_choice=="rock" and computer_choice=="scissors":
        print("you win")
    elif user_choice=="paper" and computer_choice=="rock":
        print("you win")
    elif user_choice=="scissors" and computer_choice=="paper":
        print("you win")
    else:
        print("you lose")
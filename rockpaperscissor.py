#simple Rock-Paper-Scissors game
import random
choice = ["Rock","Paper","Scissor"]
computer = random.choice(choice)
user = input("Enter your choice (Rock, Paper, Scissor): ")
print(f"Computer chose: {computer}")
print(f"You chose: {user}")
if user == computer:
    print("It's a tie!")
elif(user == "Rock" and computer == "Scissor") or (user == "Paper" and computer == "Rock") or (user == "Scissor" and computer == "Paper"):
    print("You win!")
else:
    print("Computer wins!")

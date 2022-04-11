import random
rock = 'r'
paper = 'p'
scissors = 's'
mylist = [rock, paper, scissors]
print("This is rock paper scissors game")
print("[r]ock, [p]aper, [s]cissors, [q]uit")
user_choice = ''
while user_choice != 'q':
	# if user wins
	user_choice = input("Enter choice: ")
	computer_choice = random.choice(mylist)

	if user_choice == rock and computer_choice == scissors or user_choice == scissors and computer_choice == paper or user_choice == paper and computer_choice == rock:
		print(f"you win...computer choice was {computer_choice}")
	# if computer wins
	elif computer_choice == rock and user_choice == scissors or computer_choice == scissors and user_choice == paper or computer_choice == paper and user_choice == rock:
		print(f"You lose...computer choice was {computer_choice}")
	# if is a tie
	elif user_choice == computer_choice:
		print("it's a tie")
	# if user   quits
	elif user_choice == 'q':
		break
	# if wrong input
	else:
		print("Watchu doin'...let's play [r]ock, [p]aper, [s]cissors, [q]uit")
print("See you next time")

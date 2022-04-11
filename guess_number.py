import random
user_input = ""
attempt = 0
guess = random.randrange(1, 50)
print("Guess the number between 1 and 50")
print("Enter 'q' to quit.")
while user_input != guess:
	attempt += 1
	user_input = int(input("> "))
	if user_input > guess:
		print("Too high")
	elif user_input < guess:
		print("Too low")

	else:
		print(f"Yay!.. you got it in {attempt} attempt(s)")




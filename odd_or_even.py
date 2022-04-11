def odd_or_even():
	print("This tiny program checks if a digit is even or odd \n(Input 'exit' to terminate program)")
	print("****************")
	user_input = None
	while user_input != "exit":
		user_input = input("Please enter integer: ")
		if user_input.isdigit() and int(user_input) % 2 == 0:  # Checking if input is even
			print("This is an even number...Have another?")

		elif user_input.isdigit() and int(user_input) % 2 != 0:  # Checking if input is odd
			print("This is an odd number...Have another?")
		elif user_input != "exit":        # Checking if input  is "exit
			print("Invalid Entry...Try again.")

	print("Program Terminated")


odd_or_even()

def calculate_tip(bill, percentage):
	tip_percentage = (percentage / 100)
	tip = (tip_percentage * bill)  # calculates tip
	total_cost = (tip + bill)  # calculates total bill
	print(f"{percentage}% tip is ${round(tip,1)} which brings your total to ${round(total_cost,1)}")  # prints
	# total bill
	return total_cost


def share_even(num_of_people, share_cost):
	each = share_cost/num_of_people  # divides bill for each person evenly
	print(f"Each person will pay ${round(each,1)}")  # prints bill for each person


def share_uneven(num_of_people, share_amount):
	percentage_split_list = []  # list of each payment percentage to be paid by each person
	payment_split_list = []  # list of all amounts to be paid by each person
	total_percentage = 100  # total percentage to keep track of each percentage payment
	print(f"Share bill to {num_of_people} people  in percentage")

	for person in range(num_of_people):  # run to receive split for each person paying
		percentage_split = float(input("> "))  # prompts user for payment split in percentage
		percentage_split_list.append(percentage_split)  # add each person's percentage split to list
		remaining_percentage = total_percentage - percentage_split  # checks remaining percentage to be paid
		print(f"Payment Percentage left: {remaining_percentage} ")  # shows user remaining percentage
		total_percentage = remaining_percentage  # updates remaining percentage

	for split in percentage_split_list:
		payment_split = (split / 100) * share_amount  # calculate payment for person per split percentage
		payment_split_list.append(payment_split)  # adds payment result to payment list
	if sum(payment_split_list) == share_amount:  # checks if payment made is same as bill
		total_split_list = payment_split_list  # makes a total list of payment amount per percentage
		print(f"Bill split is now {total_split_list} dollars total")  # prints total bill list
	else:  # if percentage split was incorrect
		print("Percentage wasn't shared correctly to persons paying")
		print("Please restart program")


try:
	total_bill = float(input("What is the  bill for today please?\n>"))  # asks to total bill
	user_tip_percentage = float(input("What tip percentage are you giving?\n>"))  # asks for tip
	amount_cost = calculate_tip(total_bill, user_tip_percentage)  # shows total bill to be paid plus tip
	share_option = input("Would you like to share bill payment? [y/n]\n>").strip()  # asks if bill to be shared

	if share_option == "y":  # if bill to be share = yes
		people = int(input("How many people are will be paying?\n>"))  # ask number of people making payment
		share_even_option = input("Would you like to split evenly?[y/n]\n>").strip()  # asks if bill will be share
		# evenly
		if share_even_option == "y":  # if bill to be shared evenly = yes
			share_even(people, amount_cost)  # calculates bill for even payment
		elif share_even_option == "n":  # if bill to be share evenly = no
			share_uneven(people, amount_cost)  # calculates bill for uneven payment
		else:  # if other user input
			print("Option is invalid")
			print("Please restart program")

	elif share_option == "n":  # if bill to be shared = no
		calculate_tip(total_bill, user_tip_percentage)  # prints total bill
	else:  # if other user input
		print("Option is invalid")
		print("Please restart program")

except ValueError:  # if other user input
	print("Something went wrong. Restart Program")

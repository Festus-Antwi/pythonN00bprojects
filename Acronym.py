# This program ask user for full meaning of an organization or concept
# and will provide the acronym to the user.
print("Enter a text to produce its acronym")
user_input = input("Enter text: ").upper()
try:
	words = user_input.split(" ")

	char = [i[0] for i in words]
	acronym = "".join(char)
	print(acronym)
except Exception:
	print("Oops something went wrong, restart program")

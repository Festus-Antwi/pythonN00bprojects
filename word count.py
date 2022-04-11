sentence = input("Tell me what's on your mind...\n")
char = sentence.split(" ")  # Splits the string by spaces in them into char list
words = []
for i in char:
	if i.isalnum():  # Checks if characters in list is only alphanumeric
		words.append(i)  # Adds alphanumeric characters to new list: words
print(f"You've just told me what's your mind in {len(words)} word(s)")

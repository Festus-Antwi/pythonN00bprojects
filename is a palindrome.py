# This program checks a word to know if it's a palindrome.
# A palindrome is a word that remains the same when read forward or backwards

print("Enter five words to check if any is a palindrome\n")
mylist = []
palindromes = []
counter = 4
try:
	for i in range(5):
		while True:
			word = input("Enter your word: ").strip()
			if word and word.isalpha() and len(word) > 1:
				mylist.append(word)
				print("Accepted...")
				if counter != 0:
					print(f"{counter} more")
					counter -= 1
				else:
					print("Done")
				break
			else:
				print("Wrong Input, Try Again")
except EOFError:
	print("Something went wrong...restart program")

mylist_reversed = [n[::-1] for n in mylist]  # makes a list of reversed words in mylist

for original, reverse in list(zip(mylist, mylist_reversed)):  # iterates through list containing tuples\
	# of both original word and reversed word for each input [(original,reversed),(original,reversed)....]
	if original == reverse:
		palindromes.append(original)
print()
print("Checking...")
print()

if len(palindromes) == 0:
	print("Sorry, no palindromes found")
else:
	print("Palindromes found:")
	for palindrome in palindromes:
		print(palindrome)

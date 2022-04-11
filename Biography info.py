"""
This is a biography display program that collects name, date of birth, home address and email.
"""


import datetime


class Person:
	def __init__(self, name, dob, address, goal):
		self.name = name
		self.dob = dob
		self.address = address
		self.goal = goal

	def show(self):
		return f"Name: {self.name}\nDate of birth: {self.dob}\nHome Address: {self.address}\nEmail Address: {self.goal}"

	@classmethod
	def from_string(cls, person_str):
		name, dob, address, goal = person_str.split("*")
		return cls(name, dob, address, goal)


def make_date(y, m, d):
	date = datetime.date(y, m, d)
	date = date.strftime("%B %d, %Y")
	return date


while True:
	name_str = input("What's your name:\n> ").strip().capitalize()
	if len(name_str) > 1:
		break
	else:
		print("Sorry, enter name correctly")

while True:
	date_str = input("What's your date of birth (dd/mm/yyyy):\n> ").strip()
	try:
		day, month, year = date_str.split("/")

		day = int(day)
		month = int(month)
		year = int(year)

		try:
			birthday = make_date(year, month, day)
			break
		except ValueError:
			print("Date does not exist...Try again")

	except:
		print("Date Incorrect...Check format")

while True:
	address_str = input("What's your home address:\n> ").strip()
	if len(address_str) > 1:
		break
	else:
		print("Invalid home address...Try again")

while True:
	email_str = input("What's your email address:\n> ").strip()
	if "@" in email_str and email_str.endswith(".com") and email_str[email_str.index("@") + 1] != "." and email_str[
		0] != "@":
		break
	else:
		print("Invalid email...Try again")

person_info = [name_str, birthday, address_str, email_str]

person_1_str = "*".join(person_info)

person1 = Person.from_string(person_1_str)

print(person1.show())

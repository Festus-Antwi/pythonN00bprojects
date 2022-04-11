import random
print("This program generates hard passwords")
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%^&*'
numbers = '0123456789'

upper_list = [random.choice(upper_case) for i in range(4)]
lower_list = [random.choice(lower_case) for x in range(4)]
symbols_list = [random.choice(symbols) for y in range(4)]
numbers_list = [random.choice(numbers) for z in range(4)]

gen_list = list(upper_list + lower_list + numbers_list + symbols_list)
random.shuffle(gen_list)
password = "".join(gen_list)
print(f"Password: {password}")

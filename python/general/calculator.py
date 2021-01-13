numbers = int(input("Cing, please enter your number: "))

total = 0
while numbers != -1:
	total += numbers
	numbers = int(input("Cing, Do you have more numbers? "))

print(f'\nYour total amout is: {total}')
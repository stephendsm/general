numbers = int(input("Cing, please enter your number: "))

total = 0
while numbers != -1:
    total += numbers
    numbers = int(input("Cing, please enter your number: "))

print(f'\nYour total amount is: {total}')

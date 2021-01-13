#coaching a hockey team
#have a list of jersay numer 1~50 except [2, 5, 12, 33, 17]

numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still available")
for i in range(1, 20):
    if i in numbersTaken:
        continue; #skip this number and go back a loop(i.e for loop)
    print(i)
#Sets = a collection of items but it cant have any duplicates like a list can
#likes a list but make sure to use '{}'
#it prints everythin on our list however it only prints once 
# (i.e you wont have the same item twice)(eg; 'beer' under example)

groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
    print("You already have milk hoss!")
else:
    print("Oh yea, yo need milk")


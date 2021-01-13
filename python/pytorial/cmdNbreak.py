#Comments, Break and Continue

'''
magicNumber = 26

for i in range(101):
    if i is magicNumber:
        print(i, " is the magic number!")
        break
    else:
        print(i)
'''

for i in range(101):
    if i%4 is 0:
        print(i, " is the magic number!")
    else:
        print(i)
        
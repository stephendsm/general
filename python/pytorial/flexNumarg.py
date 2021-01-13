#Flexible number of arguments
#We dont know how many argument the user gonna have
#So we can have a flexible amount of argument by adding '*' in our function(i.e def fun(*keyword))

def add_number(*argc):
    total = 0
    for i in argc:
        total += i
    print(total)

add_number(3)
add_number(3, 5)
add_number(3, 5, 10, 25)



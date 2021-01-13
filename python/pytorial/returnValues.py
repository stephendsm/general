#we had a function and print it out somethin (see functio.py)
#In some cases, we want a function to do something but not print it out right then and there
#store the answer or the response so we can use it later in our program
#this can be done by useing return statement

#A function which calculates the age of girl that u r allowed to date
#(i.e cannt date a girls under 13 for example)

def allowed_dating_age(my_age):
    girl_age = my_age/2 + 7
    return girl_age

stephen_limit = allowed_dating_age(37)
print("Stephen can date girls of ages", stephen_limit, "or older")

'''
# __init__ is a special type of funtion that gets call automatically whenever you create an object(i.e you dont have to call it explicitly)
class Tuna:
    def __init__(self): # __init__ = initialize or something
        print('Baølksjdfasd')

    def swim(self):
        print('I am swimming')

# We can see that __init__ is called firstly whenever function we called (swim() function in this case)
flipper = Tuna()
flipper.swim()
'''
#Practical example of what it is useful
class Enemy_a:
    def __init__(self, x): # Everytime we create an object('enemy1' ..),I want to give them a certain amount of energy
        self.energy = x

    def get_energy(self):
        print(self.energy)

json = Enemy_a(6)
emma = Enemy_a(18)

json.get_energy()
emma.get_energy()

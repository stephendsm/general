# Make a group of similar variables and functions together
class Enemy: # Naming begin with a captial letter is a common practice, differentiate btw noral variable and class
    life = 3 # each enemy has a life of 3, ofcoz this life variable is part of 'Enamy' class

    # Make a couple function for this class 'Enemy'
    def attack(self): # this is just some what happens whenever we attack an enemy
                      #(self) = object, i.e use something from this own class 'Enemy'
                      #self.attack means use the attack function in this class 'Enemy'
                      #self.life means use the life variable in this class 'Enemy'
        print("ouch!")#dead of something
        #since one of the enemy dead, ofcoz it needs to be substracted
        #cant just do like this(life -= 1)
        self.life -= 1 #that is how we access the variables inside our class 'Enemy'
                       #so pretty much 'self' is saying ok, inside this class 'Enemy', take away 1 from the 'life' variable
    def checklife(self):
        if self.life <= 0: # '<=0' bcoz if the enemy life of 5 was slash with a weapon, it would be '-2' or something so..
            print("I am dead")
        else:
            print(str(self.life) + 'life left')

#In order to use anything inside our class, we need to access it a specialy way(cant do like this..attack())
#That is by creating something called an 'object'
#Object: it's pretty much a way that we can access the stuff inside our class 
#So the first thing we do is we pretty much act like we are making a normal variable
#So I'm going to make a object called 'enemy1' and set = to the class that you want to use stuff from
enemy1 = Enemy()

enemy1.attack()

enemy1.checklife()

# cool thing to notice
# Each object(i.e 'enemy1' is one object) is independent of one another
enemy2 = Enemy()
enemy2.attack()
enemy2.checklife()
# One class is pretty much a templete of how do you want (to code the enemy/it to behave)
# i.e You can create as many of them as you want just by making an object for each one
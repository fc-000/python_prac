#Inheritance example from Programiz

#base class
class Animal:

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

class Dog(Animal):

    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog() 

# Calling members of the base class
dog1.eat()
dog1.sleep()


# Calling members of the derived class
dog1.bark();


# Multiple Inheritance - A mechanism where a new class can inherit
# properties and behavior (methods) from more than one existing class.

class Prey:
    def flee(self):
        print("The prey is fleeing!")

class Predator:
    def hunt(self):
        print("The predator is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
print("Rabbit:")
rabbit.flee()
print("\nHawk:")
hawk.hunt()
print("\nFish:")
fish.flee()
fish.hunt()
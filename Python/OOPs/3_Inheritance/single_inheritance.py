# Inheritance - A mechanism where a new class inherits 
# properties and behavior (methods) from an existing class.

# Example of Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Spike")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(f"Dog: {dog.name}, Alive: {dog.is_alive}")
dog.eat()
dog.sleep()
dog.speak()
# Class - Blueprint for creating real-world objects containing attributes and methods
# Attributes - Characteristics of an object
# Methods - Actions that an object can perform
# Object - Instance of a class

class Car:
    def __init__(self, model, year, color, for_sale):
        # Attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods
    def drive(self):
        print(f"You drive the {self.model}.")
    
    def stop(self):
        print(f"You stop the {self.model}.")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}, For Sale: {self.for_sale}")
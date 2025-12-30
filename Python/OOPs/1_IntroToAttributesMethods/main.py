from car import Car

car1 = Car("Toyota", 2020, "Blue", True)
car2 = Car("Honda", 2019, "Red", False)
print(f"Car 1: {car1.model}, Year: {car1.year}, Color: {car1.color}, For Sale: {car1.for_sale}")
print(f"Car 2: {car2.model}, Year: {car2.year}, Color: {car2.color}, For Sale: {car2.for_sale}")

car1.describe()
car1.drive()
car1.stop()

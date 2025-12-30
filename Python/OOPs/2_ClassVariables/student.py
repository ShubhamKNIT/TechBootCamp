# Class variables are shared across all instances of a class.
# They are defined outside of any methods(constructor),
# usually at the top of the class definition.

class Student:
    # Class variable
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

stud_1 = Student("Alice", 20)
stud_2 = Student("Bob", 22)

print(f"Student 1: {stud_1.name}, Age: {stud_1.age}")
print(f"Student 2: {stud_2.name}, Age: {stud_2.age}")

# Accessing class variable
# It's good practice to access class variables using the class name
print(f"Class Year: {Student.class_year}")
print(f"Total Students: {Student.num_students}")
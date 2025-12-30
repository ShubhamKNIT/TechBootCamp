# Static Method - A static method is a method that belongs to the class rather than any specific instance of the class.
# It does not require access to instance (self) or class (cls) variables.
# Usage: To define general utility functions that are related to the class but do not need to access instance or class data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Employee Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Developer", "Designer", "Manager", "Intern"]
        return position in valid_positions
    
if __name__ == "__main__":
    emp1 = Employee("Alice", "Developer")
    emp2 = Employee("Bob", "Chef")
    
    print(emp1.get_details())

    print(f"\nIs '{emp1.position}' a valid position? {Employee.is_valid_position(emp1.position)}")
    print(f"Is 'ML Engineer' a valid position? {Employee.is_valid_position('ML Engineer')}")
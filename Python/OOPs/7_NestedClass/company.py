# Nested Class : A class defined within another class.
# Usage: To logically group classes that are only used in one place,
# to encapsulate helper classes, or to improve code organization.

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"Employee Name: {self.name}, Position: {self.position}"
        
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        for emp in self.employees:
            print(emp.get_details())

if __name__ == "__main__":
    my_company = Company("Tech Solutions")
    my_company.add_employee("Alice", "Developer")
    my_company.add_employee("Bob", "Designer")
    
    print(f"Company: {my_company.company_name}")
    my_company.list_employees()
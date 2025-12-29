from typing import NamedTuple
from dataclasses import dataclass
import csv

@dataclass(frozen=True)
class Employee(NamedTuple):
    name: str
    age: int
    position: str = 'Python Dev'

employees = []
with open('employees.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip header row
    for name, age, position in reader:
        employees.append(Employee(name, int(age), position))

print("Employee List:")
for emp in employees:
    print(emp)

print("\nAttempting to modify an Employee instance:")
try:
    emp = Employee("John Doe", 30)
    print(emp)
    # Attempting to modify an attribute will raise an error
    emp.age = 31
except Exception as e:
    print("Error:", e)
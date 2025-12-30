# Association - A relationship between two classes where one class uses or interacts with another.
# Aggregation : Weak form of association where the contained object can exist independently of the container object.

class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teachers):
        self.teachers = teachers

t1 = Teacher("Mr. Smith")
t2 = Teacher("Ms. Johnson")
dept = Department([t1, t2])

print("Teachers in the Department:")
for teacher in dept.teachers:
    print(teacher.name)

print("Deleting the Department...")
del dept  # Deleting the Department object

print(f"Teacher 1 still exists: {t1.name}")
print(f"Teacher 2 still exists: {t2.name}")

try:
    print("Accessing deleted Department's teachers:")
    print(dept.teachers)
except NameError:
    print("Error: Department object has been deleted, but Teacher objects still exist.")
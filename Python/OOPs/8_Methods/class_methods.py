# Class Method - A class method is a method that is bound to the class and not the instance of the class.
# It takes (cls) as the first parameter which points to the class and not the object instance.
# Usage: To create factory methods that can instantiate objects using different parameters or to access/modify class-level data.

class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # Instance Method
    def get_info(self):
        return f"Student Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"
    

if __name__ == "__main__":
    student1 = Student("John", 3.5)
    student2 = Student("Jane", 3.8)
    
    print(student1.get_info())
    print(student2.get_info())

    # Calling class method using the class name
    print(Student.get_count())

    # Calling instance method using the class name will raise an error
    try:
        print(Student.get_info())
    except TypeError as e:
        print(f"\nError: {e} - 'get_info' is an instance method and requires an instance to be called.")
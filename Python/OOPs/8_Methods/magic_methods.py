# Magic Methods in Python - Also known as Dunder Methods (Double Underscore Methods)
# These methods allow you to define the behavior of your objects with respect to built-in operations.
# Usage: To customize object behavior for operations like addition, string representation, length calculation, etc

# Method Overloading using Magic Methods

from typing import Any


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.pages == other.pages)
        return False
    
    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return f"KeyError: {key} not found in Book attributes"
        
    
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    
    print(book1)  # Calls __str__ method
    print(book2)  # Calls __str__ method

    print(book1 == book2)  # Default behavior, compares memory addresses, if not overridden
    print(book1 == Book("1984", "George Orwell", 328))  # Calls __eq__ method.

    print("1984" in book1)  # Calls __contains__ method
    print("Harper" in book1)  # Calls __contains__ method

    print(book1['title'])  # Calls __getitem__ method
    print(book2['author'])  # Calls __getitem__ method
    print(book2['pages'])  # Calls __getitem__ method
    print(book2['publisher'])  # Raises KeyError
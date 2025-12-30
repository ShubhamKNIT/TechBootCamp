# Destrutctors in Python are defined using the __del__ method.
# They are called when an object is about to be destroyed.
# Usage: To perform cleanup actions like closing files or releasing resources when an object is no longer needed.

# Generally, destructors are not commonly used in Python due to its automatic garbage collection.

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'w')
        print(f"File '{self.filename}' opened for writing.")

    def write_data(self, data):
        self.file.write(data)
        print(f"Data written to '{self.filename}'.")

    def __del__(self):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed.")

if __name__ == "__main__":
    handler = FileHandler("example.txt")
    handler.write_data("Hello, World!")
    # Deleting the object to trigger the destructor
    del handler
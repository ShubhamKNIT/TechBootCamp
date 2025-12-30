# Compostion : Strong form of association where the contained object cannot exist without the container object.

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.room = Room("Bedroom")

my_house = House()
print(f"My house has a room named: {my_house.room.name}")


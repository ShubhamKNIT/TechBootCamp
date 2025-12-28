from typing import Callable, List, NewType, TypeVar, Generic

from annotated_types import Ge

# Function that takes a callable as argument
def apply_function() -> Callable[[int, int], int]:
    func : Callable[[int, int], int] = lambda x, y: x + y
    return func

# Type aliases 
Vector = List[int]
vector : Vector = [1, 2, 3, 4, 5]
print(f"Vector: {vector}")

# New Types
userid = NewType('userid', str)
user_id: userid = userid("user_12345")
print(f"User ID: {user_id}")

# # TypeVar with constraints
# T = TypeVar('T', int, str, float)

# def add_items(item1: T, item2: T) -> T:
#     return item1 + item2

# result_int = add_items(5, 10)
# print(f"Result (int): {result_int}")
# result_str = add_items("Hello, ", "World!")
# print(f"Result (str): {result_str}")

# # TypeVar with Generic
T = TypeVar('T')
class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value
    
int_container = Container[int](42).get_value()
print(f"Container Value: {int_container}")

str_container = Container[str]("Hello").get_value()
print(f"Container Value: {str_container}")

li_container = Container[List[int]]([1, 2, 3]).get_value()
print(f"List of TypeVar: {li_container}")
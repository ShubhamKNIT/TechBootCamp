# mypy typing_module.py to check for type errors

from typing import List, Dict, Tuple, Set, Union, Optional, Any, Sequence, Literal

# Examples of type hints using typing module
li : List[int] = [1, 2, 3]
d : Dict[str, int] = {"a": 1, "b": 2}
u : Union[int, str] = "hello"
s : Set[str] = {"apple", "banana", "cherry"}
o : Optional[int] = None

# Tuple with different types
t : Tuple[int, str, float] = (1, "hello", 3.14)

# List with any type of elements
li_any : List[Any] = [1, "two", 3.0, [4, 5]]

# Sequence can be used for both lists and tuples
seq_str_t : Sequence[str] = ("apple", "banana", "cherry")
seq_str_li : Sequence[str] = ["dog", "cat", "mouse"]

# Literal type hint (more like an enum)
lit: Literal['red', 'green', 'blue'] = 'red'
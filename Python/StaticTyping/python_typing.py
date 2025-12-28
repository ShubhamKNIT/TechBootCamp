x : int = 4 # int is the type hint and shouldn't be treated as type of variable

y : str = 5

# this programs will run without any error even though the type hints are violated
# but static type checkers like mypy will raise errors when checking the code
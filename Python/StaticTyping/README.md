# Static Typing in Python

- `typing` - python module which allows type hinting
- `mypy`, `pyright`, `pyre` - bash tool which checks type annotations correctness
- `pydantic` - 3rd party python library which does type validation during runtime


## `mypy` type checking

- Create a file with type hinting or annotation
- `pip install mypy`
- `mypy <PythonFile>`


## `pyre` type checking
- `pip install pyre-check` : 
- `pyre init` : initialize project directory
- `pyre check` : run type checking
- `pyre watch` : watches files in runtime and flags if any issues

### Building Python Extension in C

#### Demo Standards:

1. Simple factorail function has been used.
2. The code has been written in Python.
3. Python-C Extensions with/without GIL.
4. While for the executing the code, 2 programs has been written.
    
    - `main.py` - This program uses Python code.
    - `fast_main.py` - This program uses C-Python Extension Module for Python code.

5. `time.perf_counter()` is used to measure the performance of the code.
6. `20s` of code execution with `main.py`
7. `0.02-0.08s` of code execution with `fast_main.py`
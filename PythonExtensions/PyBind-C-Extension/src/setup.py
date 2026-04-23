from setuptools import setup, Extension
import pybind11

ext_mdodules = [
    Extension(
        "math_module",
        ["module.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="math_module",
    version="0.1",
    ext_modules=ext_mdodules
)
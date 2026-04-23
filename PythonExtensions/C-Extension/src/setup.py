from setuptools import setup, Extension

setup(
    name="fast_factorial_module",
    version="0.1.0",
    ext_modules=[
        Extension(
            "fast_factorial_module",
            ["fast_factorial.c"],
        )
    ]
)
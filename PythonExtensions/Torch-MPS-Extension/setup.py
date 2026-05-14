from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(
    name='torch_mps_extension',
    ext_modules=[
        CppExtension(
            'my_mps_extension',
            [
                'binding.cpp',
                'op_cpu.cpp',
                'op_mps.mm'
            ],
            extra_compile_atgs={
                'cxx': ['-03'],
            }
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='my_extension',
    ext_modules=[
        CUDAExtension(
            'my_extension',
            [
                'binding.cpp',
                'kernel.cu',
            ],
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
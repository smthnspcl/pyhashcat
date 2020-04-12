from setuptools import setup, Extension

e = Extension(
    'pyhashcat',
    include_dirs=[
        'hashcat/include',
        'hashcat/deps/OpenCL-Headers',
        'hashcat/OpenCL',
        'hashcat',
        'hashcat/deps/LZMA-SDK/C',
        'hashcat/deps/zlib',
        'hashcat/deps/zlib/contrib/minizip'
    ],
    library_dirs=["/usr/local/lib"],
    libraries=["hashcat"],
    extra_link_args=['-shared', '-Wl,-R/usr/local/lib'],
    sources=['pyhashcat/pyhashcat.c'],
    extra_compile_args=['-std=c99', '-DWITH_BRAIN',
                        '-Wimplicit-function-declaration']
)

setup(
    name='pyhashcat',
    version='5.1',
    description='Python bindings for Hashcat',
    author='Rich Kelley',
    author_email='rk5devmail@gmail.com',
    url='www.bytesdarkly.com',
    ext_modules=[e]
)

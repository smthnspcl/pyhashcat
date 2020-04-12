from setuptools import setup, Extension
from os import listdir

hc_lib_path = '/usr/local/lib'
hc_lib = 'libhashcat.so'
try:
    files = listdir(hc_lib_path)
    for f in files:
        if 'hashcat' in f:
            hc_lib = f
            break
except Exception as e:
    print(e)
    print("Unable to find libhashcat.so in %s." % hc_lib_path)
    exit()


pyhashcat_module = Extension('pyhashcat',
                             include_dirs=[
                                 'hashcat/include',
                                 'hashcat/deps/OpenCL-Headers',
                                 'hashcat/OpenCL',
                                 'hashcat'
                             ],
                             library_dirs=[hc_lib_path],
                             libraries=[hc_lib],
                             extra_link_args=['-shared', '-Wl,-R/usr/local/lib'],
                             sources=['pyhashcat.c'],
                             extra_compile_args=['-std=c99', '-DWITH_BRAIN', '-Wimplicit-function-declaration']
                             )

setup(
    name='pyhashcat',
    version='3.0',
    description='Python bindings for hashcat',
    author='Rich Kelley',
    author_email='rk5devmail@gmail.com',
    url='www.bytesdarkly.com',
    ext_modules=[pyhashcat_module]
)

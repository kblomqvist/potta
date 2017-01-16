import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('potta/potta.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="potta",
    version=__version__,
    description="MCU",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "yasha",
        "scons",
    ],
    entry_points='''
        [console_scripts]
        potta=potta.scripts.potta:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
    ],
    url="https://github.com/kblomqvist/potta",
    download_url="https://github.com/kblomqvist/potta/tarball/" + __version__,
)

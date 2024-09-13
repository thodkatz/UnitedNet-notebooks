from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="mongoose",
    version="0.0.0",
    description="",
    long_description="",
    license="MIT Licence",
    url="",
    author="",
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "UnitedNet @ git+https://github.com/thodkatz/UnitedNet.git",
        "jupyter"
    ],
)

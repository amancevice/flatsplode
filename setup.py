from setuptools import setup
from setuptools import find_packages

setup(
    author='amancevice',
    author_email='smallweirdnumber@gmail.com',
    description='Flatten/explode JSON objects.',
    name='flatsplode',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools_scm'],
    url="http://github.com/amancevice/flatsplode",
    use_scm_version=True,
)

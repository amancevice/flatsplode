from setuptools import (find_packages, setup)

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    author='amancevice',
    author_email='smallweirdnum@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
    description='Flatten/explode JSON objects',
    name='flatsplode',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    python_requires='>= 3.5',
    setup_requires=['setuptools_scm'],
    tests_require=[
        'flake8',
        'pytest',
        'pytest-cov',
    ],
    url='http://github.com/amancevice/flatsplode',
    use_scm_version=True,
)

# Flatsplode

[![Build Status](https://travis-ci.com/amancevice/flatsplode.svg?branch=master)](https://travis-ci.com/amancevice/flatsplode)
[![PyPI Version](https://badge.fury.io/py/flatsplode.svg)](https://badge.fury.io/py/flatsplode)
[![Test Coverage](https://api.codeclimate.com/v1/badges/974cfe08c8e29ab4d1d2/test_coverage)](https://codeclimate.com/github/amancevice/flatsplode/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/974cfe08c8e29ab4d1d2/maintainability)](https://codeclimate.com/github/amancevice/flatsplode/maintainability)

Flatten/Explode JSON objects.

## Installation

```bash
pip install flatsplode
```

## Usage

Use the `flatsplode()` function to recursively flatten and explode complex JSON objects.

Import the `flatsplode` function:

```python
from flatsplode import flatsplode
```

Create a sample object to flatsplode:

```python
item = {
    'id': '78e5b18c',
    'keywords': [
        'fizz',
        'buzz'
    ],
    'attrs': [
        {'name': 'color', 'value': 'green'},
        {'name': 'size', 'value': 42},
    ],
    'deep': {
        'nested': {
            'keys': {
                'fizz': 'buzz',
                'jazz': 'fuzz',
            }
        }
    }
}
```

Calling `flatsplode(item)` will return a generator. Use `list()` to expand:


```python
list(flatsplode(item))

[
    {
        'id': '78e5b18c',
        'keywords': 'fizz',
        'attrs.name': 'color',
        'attrs.value': 'green',
        'deep.nested.keys.fizz': 'buzz',
        'deep.nested.keys.jazz': 'fuzz'
    },
    {
        'id': '78e5b18c',
        'keywords': 'fizz',
        'attrs.name': 'size',
        'attrs.value': 42,
        'deep.nested.keys.fizz': 'buzz',
        'deep.nested.keys.jazz': 'fuzz'
    },
    {
        'id': '78e5b18c',
        'keywords': 'buzz',
        'attrs.name': 'color',
        'attrs.value': 'green',
        'deep.nested.keys.fizz': 'buzz',
        'deep.nested.keys.jazz': 'fuzz'
    },
    {
        'id': '78e5b18c',
        'keywords': 'buzz',
        'attrs.name': 'size',
        'attrs.value': 42,
        'deep.nested.keys.fizz': 'buzz',
        'deep.nested.keys.jazz': 'fuzz'
    }
]
```

Flatsploding is useful when converting objects to pandas DataFrame matrices:

```python
import pandas
from flatsplode import flatsplode

pandas.DataFrame(list(flatsplode(item)))
```

```
         id attrs.name attrs.value deep.nested.keys.fizz deep.nested.keys.jazz keywords
0  78e5b18c      color       green                  buzz                  fuzz     fizz
1  78e5b18c       size          42                  buzz                  fuzz     fizz
2  78e5b18c      color       green                  buzz                  fuzz     buzz
3  78e5b18c       size          42                  buzz                  fuzz     buzz
```

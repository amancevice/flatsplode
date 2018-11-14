# Flatsplode

[![build](https://travis-ci.org/amancevice/flatsplode.svg?branch=master)](https://travis-ci.org/amancevice/flatsplode)
[![codecov](https://codecov.io/gh/amancevice/flatsplode/branch/master/graph/badge.svg)](https://codecov.io/gh/amancevice/flatsplode)
[![pypi](https://badge.fury.io/py/flatsplode.svg)](https://badge.fury.io/py/flatsplode)

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

pandas.DataFrame(list(flatsplode(item))).set_index('id')
```

```
         id attrs.name attrs.value deep.nested.keys.fizz deep.nested.keys.jazz keywords
0  78e5b18c      color       green                  buzz                  fuzz     fizz
1  78e5b18c       size          42                  buzz                  fuzz     fizz
2  78e5b18c      color       green                  buzz                  fuzz     buzz
3  78e5b18c       size          42                  buzz                  fuzz     buzz
```

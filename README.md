# Flatsplode

[![pypi](https://img.shields.io/pypi/v/flatsplode?color=yellow&logo=python&logoColor=eee&style=flat-square)](https://pypi.org/project/flatsplode/)
[![python](https://img.shields.io/pypi/pyversions/flatsplode?logo=python&logoColor=eee&style=flat-square)](https://pypi.org/project/flatsplode/)
[![pytest](https://img.shields.io/github/workflow/status/amancevice/flatsplode/pytest?logo=github&style=flat-square)](https://github.com/amancevice/flatsplode/actions)
[![coverage](https://img.shields.io/codeclimate/coverage/amancevice/flatsplode?logo=code-climate&style=flat-square)](https://codeclimate.com/github/amancevice/flatsplode/test_coverage)
[![maintainability](https://img.shields.io/codeclimate/maintainability/amancevice/flatsplode?logo=code-climate&style=flat-square)](https://codeclimate.com/github/amancevice/flatsplode/maintainability)

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

You can also provide your own join-character:

```python
list(flatsplode(item, '/'))

[
    {
        'id': '78e5b18c',
        'keywords': 'fizz',
        'attrs/name': 'color',
        'attrs/value': 'green',
        'deep/nested/keys/fizz': 'buzz',
        'deep/nested/keys/jazz': 'fuzz'
    },
    …
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

import pytest

from flatsplode import (explode, flatsplode, flatten)


@pytest.mark.parametrize(('item', 'exp'), [
    (
        {
            'a': 'b',
            'b': [],
            'jar': ['bar', 'car'],
            'fizz': ['buzz', 'jazz', 'fuzz'],
            'foo': 'bar',
        },
        [
            {'a': 'b', 'b': None, 'jar': 'bar', 'fizz': 'buzz', 'foo': 'bar'},
            {'a': 'b', 'b': None, 'jar': 'bar', 'fizz': 'jazz', 'foo': 'bar'},
            {'a': 'b', 'b': None, 'jar': 'bar', 'fizz': 'fuzz', 'foo': 'bar'},
            {'a': 'b', 'b': None, 'jar': 'car', 'fizz': 'buzz', 'foo': 'bar'},
            {'a': 'b', 'b': None, 'jar': 'car', 'fizz': 'jazz', 'foo': 'bar'},
            {'a': 'b', 'b': None, 'jar': 'car', 'fizz': 'fuzz', 'foo': 'bar'},
        ],
    ),
])
def test_explode(item, exp):
    ret = list(explode(item))
    ret.sort(key=lambda x: (x['jar'], x['fizz']))
    exp.sort(key=lambda x: (x['jar'], x['fizz']))
    assert ret == exp


@pytest.mark.parametrize(('item', 'join', 'exp'), [
    (
        {
            'fizz': {
                'buzz': {
                    'jazz': 'fuzz',
                }
            },
            'empty': {
            },
        },
        '.',
        {
            'fizz.buzz.jazz': 'fuzz',
            'empty': None,
        },
    ),
    (
        {
            'fizz': {
                'buzz': {
                    'jazz': 'fuzz',
                }
            },
            'empty': {
            },
        },
        '/',
        {
            'fizz/buzz/jazz': 'fuzz',
            'empty': None,
        },
    ),
])
def test_flatten(item, join, exp):
    ret = flatten(item, join)
    assert ret == exp


@pytest.mark.parametrize(('item', 'exp'), [
    (
        {
            'a': 'b',
            'b': [],
            'jar': ['bar', 'car'],
            'foo': {
                'fizz': [
                    {'buzz': 1, 'jazz': 2, 'fuzz': 3, 'array': [9, 8, 7]},
                    {'buzz': 2, 'jazz': 3, 'fuzz': 4, 'array': [9, 8, 7]},
                    {'buzz': 3, 'jazz': 4, 'fuzz': 5, 'array': [9, 8, 7]},
                ],
            },
        },
        [
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'bar',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 1,
                'foo.fizz.fuzz': 3,
                'foo.fizz.jazz': 2,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 2,
                'foo.fizz.fuzz': 4,
                'foo.fizz.jazz': 3,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 9,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 8,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'car',
            },
            {
                'a': 'b',
                'b': None,
                'foo.fizz.array': 7,
                'foo.fizz.buzz': 3,
                'foo.fizz.fuzz': 5,
                'foo.fizz.jazz': 4,
                'jar': 'car',
            }
        ],
    ),
    (
        {'test': [0, 0.0, [], '', 123]},
        [
            {'test': 0},
            {'test': 0.0},
            {'test': []},
            {'test': ''},
            {'test': 123},
        ]
    )
])
def test_flatsplode(item, exp):
    ret = list(flatsplode(item))
    assert ret == exp

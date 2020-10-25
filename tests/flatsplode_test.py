import pytest

from flatsplode import (explode, flatsplode, flatten)


@pytest.mark.parametrize(('item', 'exp'), [
    (
        {
            'a': 'b',
            'jar': ['bar', 'car'],
            'fizz': ['buzz', 'jazz', 'fuzz'],
            'foo': 'bar',
        },
        [
            {'a': 'b', 'jar': 'bar', 'fizz': 'buzz', 'foo': 'bar'},
            {'a': 'b', 'jar': 'bar', 'fizz': 'jazz', 'foo': 'bar'},
            {'a': 'b', 'jar': 'bar', 'fizz': 'fuzz', 'foo': 'bar'},
            {'a': 'b', 'jar': 'car', 'fizz': 'buzz', 'foo': 'bar'},
            {'a': 'b', 'jar': 'car', 'fizz': 'jazz', 'foo': 'bar'},
            {'a': 'b', 'jar': 'car', 'fizz': 'fuzz', 'foo': 'bar'},
        ],
    ),
])
def test_explode(item, exp):
    ret = list(explode(item))
    ret.sort(key=lambda x: (x['jar'], x['fizz']))
    exp.sort(key=lambda x: (x['jar'], x['fizz']))
    print(ret)
    print(exp)
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
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "bar",
            },
            {
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 1,
                "foo.fizz.fuzz": 3,
                "foo.fizz.jazz": 2,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 2,
                "foo.fizz.fuzz": 4,
                "foo.fizz.jazz": 3,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 9,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 8,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "car",
            },
            {
                "a": "b",
                "foo.fizz.array": 7,
                "foo.fizz.buzz": 3,
                "foo.fizz.fuzz": 5,
                "foo.fizz.jazz": 4,
                "jar": "car",
            }
        ],
    ),
])
def test_flatsplode(item, exp):
    ret = list(flatsplode(item))
    ret.sort(key=lambda x: (
        x['jar'],
        x['foo.fizz.array'],
        x['foo.fizz.buzz'],
        x['foo.fizz.jazz'],
        x['foo.fizz.fuzz'],
    ))
    exp.sort(key=lambda x: (
        x['jar'],
        x['foo.fizz.array'],
        x['foo.fizz.buzz'],
        x['foo.fizz.jazz'],
        x['foo.fizz.fuzz'],
    ))
    assert ret == exp

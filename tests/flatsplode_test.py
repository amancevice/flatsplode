from flatsplode import explode
from flatsplode import flatsplode
from flatsplode import flatten


def test_explode():
    item = {
        'a': 'b',
        'jar': ['bar', 'car'],
        'fizz': ['buzz', 'jazz', 'fuzz'],
        'foo': 'bar',
    }
    ret = list(explode(item))
    exp = [
        {'a': 'b', 'jar': 'bar', 'fizz': 'buzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'bar', 'fizz': 'jazz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'bar', 'fizz': 'fuzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'buzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'jazz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'fuzz', 'foo': 'bar'},
    ]
    ret.sort(key=lambda x: (x['jar'], x['fizz']))
    exp.sort(key=lambda x: (x['jar'], x['fizz']))
    print(ret)
    print(exp)
    assert ret == exp


def test_flatten():
    item = {
        'fizz': {
            'buzz': {
                'jazz': 'fuzz',
            }
        },
        'empty': {
        },
    }
    ret = flatten(item)
    exp = {
        'fizz.buzz.jazz': 'fuzz',
        'empty': None,
    }
    assert ret == exp


def test_flatsplode():
    item = {
        'a': 'b',
        'jar': ['bar', 'car'],
        'foo': {
            'fizz': [
                {'buzz': 1, 'jazz': 2, 'fuzz': 3, 'array': [9, 8, 7]},
                {'buzz': 2, 'jazz': 3, 'fuzz': 4, 'array': [9, 8, 7]},
                {'buzz': 3, 'jazz': 4, 'fuzz': 5, 'array': [9, 8, 7]},
            ],
        },
    }
    ret = list(flatsplode(item))
    exp = [
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "bar"
        },
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 1,
            "foo.fizz.fuzz": 3,
            "foo.fizz.jazz": 2,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 2,
            "foo.fizz.fuzz": 4,
            "foo.fizz.jazz": 3,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 9,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 8,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "car"
        },
        {
            "a": "b",
            "foo.fizz.array": 7,
            "foo.fizz.buzz": 3,
            "foo.fizz.fuzz": 5,
            "foo.fizz.jazz": 4,
            "jar": "car"
        }
    ]
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

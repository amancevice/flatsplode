import flatsplode


def test_explode():
    item = {
        'a': 'b',
        'jar': ['bar', 'car'],
        'fizz': ['buzz', 'jazz', 'fuzz'],
        'foo': 'bar',
    }
    ret = list(flatsplode.explode(item))
    exp = [
        {'a': 'b', 'jar': 'bar', 'fizz': 'buzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'bar', 'fizz': 'jazz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'bar', 'fizz': 'fuzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'buzz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'jazz', 'foo': 'bar'},
        {'a': 'b', 'jar': 'car', 'fizz': 'fuzz', 'foo': 'bar'},
    ]
    ret.sort(key=lambda x: x.items())
    exp.sort(key=lambda x: x.items())
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
    ret = flatsplode.flatten(item)
    exp = {
        'fizz.buzz.jazz': 'fuzz',
        'empty': None,
    }
    assert ret == exp


def test_flatsplode():
    item = {
        'a': 'b',
        'jar': ['bar', 'car'],
        'fizz': [
            {'buzz': 1, 'jazz': 2, 'fuzz': 3},
            {'buzz': 2, 'jazz': 3, 'fuzz': 4},
            {'buzz': 3, 'jazz': 4, 'fuzz': 5},
        ],
        'foo': 'bar',
    }
    ret = list(flatsplode.flatsplode(item))
    exp = [
        {
            'a': 'b',
            'jar': 'bar',
            'fizz.buzz': 1,
            'fizz.jazz': 2,
            'fizz.fuzz': 3,
            'foo': 'bar',
        },
        {
            'a': 'b',
            'jar': 'bar',
            'fizz.buzz': 2,
            'fizz.jazz': 3,
            'fizz.fuzz': 4,
            'foo': 'bar',
        },
        {
            'a': 'b',
            'jar': 'bar',
            'fizz.buzz': 3,
            'fizz.jazz': 4,
            'fizz.fuzz': 5,
            'foo': 'bar',
        },
        {
            'a': 'b',
            'jar': 'car',
            'fizz.buzz': 1,
            'fizz.jazz': 2,
            'fizz.fuzz': 3,
            'foo': 'bar',
        },
        {
            'a': 'b',
            'jar': 'car',
            'fizz.buzz': 2,
            'fizz.jazz': 3,
            'fizz.fuzz': 4,
            'foo': 'bar',
        },
        {
            'a': 'b',
            'jar': 'car',
            'fizz.buzz': 3,
            'fizz.jazz': 4,
            'fizz.fuzz': 5,
            'foo': 'bar',
        }
    ]
    ret.sort(key=lambda x: x.items())
    exp.sort(key=lambda x: x.items())
    assert ret == exp

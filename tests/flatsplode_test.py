import flatsplode


def test_explode():
    item = {
        'a': 'b',
        'jar': ['bar', 'car'],
        'fizz': ['buzz', 'jazz', 'fuzz'],
        'foo': 'bar',
    }
    ret = flatsplode.explode(item, expand=True)
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
    ret = flatsplode.flatten(item, expand=True)
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
                {'buzz': 1, 'jazz': 2, 'fuzz': 3},
                {'buzz': 2, 'jazz': 3, 'fuzz': 4},
                {'buzz': 3, 'jazz': 4, 'fuzz': 5},
            ],
        },
    }
    ret = flatsplode.flatsplode(item, expand=True)
    exp = [
        {
            'a': 'b',
            'jar': 'bar',
            'foo.fizz.buzz': 1,
            'foo.fizz.jazz': 2,
            'foo.fizz.fuzz': 3,
        },
        {
            'a': 'b',
            'jar': 'bar',
            'foo.fizz.buzz': 2,
            'foo.fizz.jazz': 3,
            'foo.fizz.fuzz': 4,
        },
        {
            'a': 'b',
            'jar': 'bar',
            'foo.fizz.buzz': 3,
            'foo.fizz.jazz': 4,
            'foo.fizz.fuzz': 5,
        },
        {
            'a': 'b',
            'jar': 'car',
            'foo.fizz.buzz': 1,
            'foo.fizz.jazz': 2,
            'foo.fizz.fuzz': 3,
        },
        {
            'a': 'b',
            'jar': 'car',
            'foo.fizz.buzz': 2,
            'foo.fizz.jazz': 3,
            'foo.fizz.fuzz': 4,
        },
        {
            'a': 'b',
            'jar': 'car',
            'foo.fizz.buzz': 3,
            'foo.fizz.jazz': 4,
            'foo.fizz.fuzz': 5,
        }
    ]
    ret.sort(key=lambda x: (
        x['jar'], x['foo.fizz.buzz'], x['foo.fizz.jazz'], x['foo.fizz.fuzz']
    ))
    exp.sort(key=lambda x: (
        x['jar'], x['foo.fizz.buzz'], x['foo.fizz.jazz'], x['foo.fizz.fuzz']
    ))
    assert ret == exp

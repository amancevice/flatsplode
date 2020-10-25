"""
flatsplode.
"""
import itertools

LIST_TYPES = (list, tuple)


def explode(item):
    """ Explode JSON object with list values.

        :param dict item: Object to explode

        :Example:

        >>> explode({'fizz': ['buzz', 'jazz', 'fuzz']})
    """
    # Collect item values that are lists/tuples
    lists = (
        [(k, x) for x in v]
        for k, v in item.items()
        if isinstance(v, (list, tuple))
    )
    # Calculate combinations of values in each list
    combos = map(dict, itertools.product(*lists))
    # Yield each combination
    for combo in combos:
        xitem = item.copy()
        xitem.update(combo)
        yield xitem


def flatsplode(item, join='.'):
    """ Explode & flatten JSON object with list values.

        :param dict item: Object to explode

        :Example:

        >>> flatsplode({'fizz': [{'key': buzz'}, {'key': 'jazz'}]})
    """
    for expl in explode(item):
        flat = flatten(expl, join)
        items = filter(lambda x: isinstance(x, LIST_TYPES), flat.values())
        if any(items):
            yield from flatsplode(flat, join)
        else:
            yield flat


def flatten(item, join='.'):
    """ Flattens nested JSON object.

        :param dict item: Object to flatten

        :Example:

        >>> flatten({'fizz': {'buzz': {'jazz': 'fuzz'}}})
    """
    return dict(iterkv(item, (), join))


def iterkv(item, parents=(), join='.'):
    """ Iterate over key/values of item recursively.

        :param dict item: Item to flatten
        :param tuple parents: Running tuple of parent keys
    """
    for key, val in item.items():
        path = parents + (key,)     # Assemble path parts
        key = str.join(join, path)  # join path parts
        val = val or None           # Yield None for empty nest

        # Yield base case
        if not isinstance(val, dict):
            yield (key, val)

        # Recurse into nested dict
        else:
            yield from iterkv(val, path, join)

"""
flatsplode.
"""
import itertools


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


def flatsplode(item):
    """ Explode & flatten JSON object with list values.

        :param dict item: Object to explode

        :Example:

        >>> flatsplode({'fizz': [{'key': buzz'}, {'key': 'jazz'}]})
    """
    for expl in explode(item):
        flat = flatten(expl)
        listvals = (x for x in flat.values() if isinstance(x, (list, tuple)))
        if any(listvals):
            for inner in flatsplode(flat):
                yield inner
        else:
            yield flat


def flatten(item):
    """ Flattens nested JSON object.

        :param dict item: Object to flatten

        :Example:

        >>> flatten({'fizz': {'buzz': {'jazz': 'fuzz'}}})
    """

    def iterkv(item, parents=()):
        """ Iterate over key/values of item recursively.

            :param dict item: Item to flatten
            :param tuple parents: Running tuple of parent keys
        """
        for key, val in item.items():

            # Recurse into nest
            if isinstance(val, dict) and val:
                for ikey, ival in iterkv(val, parents + (key,)):
                    yield (ikey, ival)

            # Yield key: None for empty nest
            elif val == {}:
                yield (key, None)

            # Yield base case
            else:
                yield ('.'.join(parents + (key,)), val)

    return dict(iterkv(item))

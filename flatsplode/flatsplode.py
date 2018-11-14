"""
flatsplode.
"""
import itertools


def explode(item, expand=False):
    """ Explode JSON object with list values.

        :param dict item: Object to explode
        :param bool expand: Flag to return list instead of generator

        :Example:

        >>> explode({"fizz": ['buzz', 'jazz', 'fuzz']})
    """

    def explodeiter(item):
        """ Iterator helper. """
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

    return explodeiter(item) if not expand else list(explodeiter(item))


def flatsplode(item, expand=False):
    """ Explode & flatten JSON object with list values.

        :param dict item: Object to explode
        :param bool expand: Flag to return list instead of generator

        :Example:

        >>> flatsplode({"fizz": [{'key': buzz'}, {'key': 'jazz'}]})
    """
    flattened = dict(flatten(item))
    exploded = explode(flattened)
    flatsploded = (flatten(x, expand) for x in exploded)
    return flatsploded if not expand else list(flatsploded)


def flatten(item, expand=False):
    """ Flattens nested JSON object.

        :param dict item: Object to flatten
        :param bool expand: Flag to return list instead of generator

        :Example:

        >>> flatten({"fizz": {"buzz": {"jazz": "fuzz"}}})
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

    return iterkv(item) if not expand else dict(iterkv(item))

"""
flatsplode utilities.
"""

import decimal
import json
from datetime import date


def jprint(obj, **kwargs):
    """Helper to print JSON."""
    params = {"default": jsonify, "indent": 4, "sort_keys": True, **kwargs}
    print(json.dumps(obj, **params))


def jsonify(value):
    """Helper to JSON-dump datetimes.

    :param object value: Object to convert to JSON-friendly value
    :returns: JSON-friendly value representation of object

    :Example:

    >>> jsonify(datetime(2018, 9, 1))
    >>> json.dumps({"time": datetime(2018, 9, 1)}, default=jsonify)
    """
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, decimal.Decimal):
        return float(value)
    raise TypeError

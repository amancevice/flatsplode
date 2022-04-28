import argparse
import io
import json
import sys

from . import __version__
from .flatsplode import (explode, flatten, flatsplode)


def main(args):
    if args.JSON == '-':  # pragma: no cover
        stream = sys.stdin
    else:
        stream = io.StringIO(args.JSON)

    if args.no_explode and args.no_flatten:
        item = json.load(stream)
    elif args.no_explode:
        item = dict(flatten(json.load(stream)))
    elif args.no_flatten:
        item = list(explode(json.load(stream)))
    else:
        item = list(flatsplode(json.load(stream)))

    return item


if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser(
        description='Flatten/explode JSON objects',
        prog='flatsplode',
        usage='%(prog)s [OPTIONS] [JSON]')
    parser.add_argument(
        '-V', '--version',
        action='version',
        version=__version__)
    parser.add_argument(
        '-F', '--no-flatten',
        action='store_true',
        help='Do not flatten')
    parser.add_argument(
        '-X', '--no-explode',
        action='store_true',
        help='Do not explode')
    parser.add_argument('JSON', help='Item JSON')
    args = parser.parse_args()
    json.dump(main(args), sys.stdout)

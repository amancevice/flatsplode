import argparse
import io
import json
import sys

from . import __version__
from .flatsplode import (explode, flatten, flatsplode)

parser = argparse.ArgumentParser(
    description='Flatten/explode JSON objects',
    prog='flatsplode',
    usage='python -m %(prog)s')
parser.add_argument(
    '--fullname',
    action='version',
    help='Show full name',
    version=f'%(prog)s-{__version__}')
parser.add_argument(
    '--name',
    action='version',
    help='Show name',
    version='%(prog)s')
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

if args.JSON == '-':
    stream = sys.stdin
else:
    stream = io.StringIO(args.JSON)

if args.no_flatten:
    item = list(explode(json.load(stream)))
elif args.no_explode:
    item = dict(flatten(json.load(stream)))
else:
    item = list(flatsplode(json.load(stream)))

json.dump(item, sys.stdout)
# print(args)

import decimal
import json
from datetime import date
from datetime import datetime
from unittest import mock

import pytest

from flatsplode import utils


def test_jsonify():
    ret = json.dumps({
        'int': 1,
        'float': 2.0,
        'date': date(2018, 8, 30),
        'datetime': datetime(2018, 8, 30, 12, 13, 14),
        'decimal': decimal.Decimal(3),
    }, default=utils.jsonify)
    exp = json.dumps({
        'int': 1,
        'float': 2.0,
        'date': '2018-08-30',
        'datetime': '2018-08-30T12:13:14',
        'decimal': 3.0,
    })
    assert ret == exp


def test_jsonify_type_error():
    with pytest.raises(TypeError):
        json.dumps({'fizz': mock.Mock()}, default=utils.jsonify)


def test_jprint():
    assert utils.jprint({}) is None

from types import SimpleNamespace

import pytest

from flatsplode.__main__ import main


@pytest.mark.parametrize(('args', 'exp'), [
    (
        SimpleNamespace(JSON='{}', no_explode=False, no_flatten=False),
        [{}],
    ),
    (
        SimpleNamespace(JSON='{}', no_explode=True, no_flatten=False),
        {},
    ),
    (
        SimpleNamespace(JSON='{}', no_explode=False, no_flatten=True),
        [{}],
    ),
    (
        SimpleNamespace(JSON='{}', no_explode=True, no_flatten=True),
        {},
    ),
])
def test_main(args, exp):
    assert main(args) == exp

"""
flatsplode
"""
from pkg_resources import (get_distribution, DistributionNotFound)

from .flatsplode import explode     # noqa: F401
from .flatsplode import flatsplode  # noqa: F401
from .flatsplode import flatten     # noqa: F401


def _version():
    """
    Helper to get package version.
    """
    try:
        return get_distribution(__name__).version
    except DistributionNotFound:  # pragma: no cover
        return None


__version__ = _version()

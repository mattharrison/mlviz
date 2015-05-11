"""Package for mlviz."""

import sys

__project__ = 'mlviz'
__version__ = '0.0.0'

VERSION = __project__ + '-' + __version__

PYTHON_VERSION = 2, 7

if not sys.version_info >= PYTHON_VERSION:  # pragma: no cover (manual test)
    exit("Python {}.{}+ is required.".format(*PYTHON_VERSION))

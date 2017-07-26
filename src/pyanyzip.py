# python 3
# import bz2
from typing import Any

from pypipegzip import pypipegzip
# python 3
# import lzma
# python 2
# import pylzma

methods = {
    "magic",
    "suffix",
}

types = {
    "plain",
    "gzip",
    "bz2",
    "xz",
}


def _get_type(name, method):
    if method == 'suffix':
        if name.endswith('.gz'):
            return 'gzip'
        if name.endswith('.bz2'):
            return 'bz2'
        if name.endswith('.xz'):
            return 'xz'
        return 'plain'
    if method == 'magic':
        raise ValueError("magic is still not implemented")


real_open = open


# noinspection PyShadowingBuiltins
def open(name, mode=None, method='suffix', type=None):
    # type: (str, str, str, str) -> Any
    global real_open
    assert method in methods
    if type is None:
        type = _get_type(name, method)
    else:
        assert type in types
    if type == 'plain':
        return real_open(name, mode=mode)
    if type == "gzip":
        return pypipegzip.open(filename=name, mode=mode)
    if type == "xz":
        # python3
        # return lzma.open(filename=name, mode=mode)
        # python2
        # return pylzma.open(filename=name, mode=mode)
        raise ValueError("xz not supported")
    if type == "bzip2":
        # python3
        # return bz2.open(filename=name, mode=mode)
        # python2
        raise ValueError("bzip2 not supported")
    raise ValueError("You should not be here")

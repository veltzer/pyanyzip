from typing import Any

import sys
from pypipegzip import pypipegzip


def is_2():
    return sys.version_info[0] == 2


def is_3():
    return sys.version_info[0] == 3

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
        if is_3():
            import lzma
            return lzma.open(filename=name, mode=mode)
        else:
            raise ValueError("xz not supported")
    if type == "bzip2":
        if is_3():
            import bz2
            return bz2.open(filename=name, mode=mode)
        else:
            raise ValueError("bzip2 not supported")
    raise ValueError("You should not be here")

import codecs
from typing import Any, Union

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


DEFAULT_ENCODING = 'utf-8'


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


if is_2():
    import io
    real_open = io.open
else:
    real_open = open


# noinspection PyShadowingBuiltins
def open(name, mode=None, method='suffix', type=None, newline=None):
    # type: (str, str, str, str, Union[str, None]) -> Any
    global real_open
    assert method in methods
    if type is None:
        type = _get_type(name, method)
    else:
        assert type in types
    if type == 'plain':
        if is_2():
            handle = real_open(name, mode=mode, newline=newline)
            return codecs.getreader(encoding=DEFAULT_ENCODING)(handle)
        else:
            return real_open(name, mode=mode, newline=newline)
    if type == "gzip":
        return pypipegzip.open(filename=name, mode=mode, newline=newline)
    if type == "xz":
        if is_3():
            import lzma
            return lzma.open(filename=name, mode=mode, newline=newline)
        else:
            raise ValueError("xz not supported")
    if type == "bzip2":
        if is_3():
            import bz2
            return bz2.open(filename=name, mode=mode, newline=newline)
        else:
            raise ValueError("bzip2 not supported")
    raise ValueError("You should not be here")

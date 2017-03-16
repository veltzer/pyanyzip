import builtins
import bz2

from pypipegzip import pypipegzip
import lzma

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


# noinspection PyShadowingBuiltins
def open(name: str, mode: str=None, method: str='suffix', type: str=None):
    assert method in methods
    if type is None:
        type = _get_type(name, method)
    else:
        assert type in types
    if type == 'plain':
        return builtins.open(name, mode=mode)
    if type == "gzip":
        return pypipegzip.open(filename=name, mode=mode)
    if type == "xz":
        return lzma.open(filename=name, mode=mode)
    if type == "bzip2":
        return bz2.open(filename=name, mode=mode)
    raise ValueError("You should not be here")

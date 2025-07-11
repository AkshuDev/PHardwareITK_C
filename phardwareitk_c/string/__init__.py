# Base funcs
from phardwareitk.Extensions import C as _mmodc

# Fellow IDE users
from typing import *

# Header imports
from phardwareitk_c import *
from phardwareitk_c.stdint import *

# mem*
memcpy = _mmodc.memcpy
memmove = _mmodc.memmove
memset = _mmodc.memset
memcmp = _mmodc.memcmp
memchr = _mmodc.memchr

# str*
def strcpy(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR) -> _mmodc.CHAR_PTR:
    """Copies a string from source to destination"""
    size = _mmodc.get_size_metadata(src.address - 8)
    return memcpy(dest, src, size).cast(char)

def strncpy(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR, n:Union[int, size_t]) -> _mmodc.CHAR_PTR:
    """Copies a string of size [bytes] from source to destination"""
    size = 0

    if isinstance(n, size_t):
        size = n
    elif isinstance(n, int):
        size = n
    else:
        raise TypeError("Type of arg 'n' has to be a size_t")

    return memcpy(dest, src, size).cast(char)

def strcat(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR) -> _mmodc.CHAR_PTR:
    """Appends a string from source to destination"""
    size = _mmodc.get_size_metadata(src.address - 8)
    # TODO: Implement

def strncat(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR, n:Union[int, size_t]) -> _mmodc.CHAR_PTR:
    """Appends a string of size [bytes] from source to destination"""
    size = 0

    if isinstance(n, size_t):
        size = n
    elif isinstance(n, int):
        size = n
    else:
        raise TypeError("Type of arg 'n' has to be a size_t")

    # TODO: Implement

def strcmp(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR) -> int_:
    """Compares strings from source and destination"""
    size = _mmodc.get_size_metadata(src.address - 8)
    return memcmp(dest, src, size).cast(char)


def strncat(dest:_mmodc.CHAR_PTR, src:_mmodc.CHAR_PTR, n:Union[int, size_t]) -> int_:
    """Compares strings of size [bytes] from source and destination"""
    size = 0

    if isinstance(n, size_t):
        size = n
    elif isinstance(n, int):
        size = n
    else:
        raise TypeError("Type of arg 'n' has to be a size_t")

    return memcmp(dest, src, size)

def strlen(str:_mmodc.CHAR_PTR) -> size_t:
    """Returns the length of a string excluding null terminators"""
    str = _mmodc.get_string(str)
    return size_t(len(str))


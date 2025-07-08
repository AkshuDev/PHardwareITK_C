# Basic Needs
from phardwareitk_c import *
from phardwareitk.Extensions import C as _mmodc
import math
# C libs
from phardwareitk_c.stdint import *
from phardwareitk_c.stddef import *

size_t = size_t # Well idk why but the real stdlib also does this.
wchar_t = wchar_t # again idk why but the real stdlib also does this.

div_t = _mmodc.Struct({
    "quot": {"type": int_, "value": None},
    "rem": {"type": int_, "value": None}
})

ldiv_t = _mmodc.Struct({
    "quot": {"type": long, "value": None},
    "rem": {"type": long, "value": None}
})

lldiv_t = _mmodc.Struct({
    "quot": {"type": long_long, "value": None},
    "rem": {"type": long_long, "value": None}
})

# Macros
NULL = NULL # ((void*)0)
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
RAND_MAX = 0 # TODO: Implement this properly
MB_CUR_MAX = 1 # TODO: Implement this properly

# Functions
def abort() -> None:
    """Aborts the program."""
    exit(EXIT_FAILURE) # Well our py does have a garbage collector so i guess not 100% C accuracy here as C just exits no cleanup

def _exit(status:Union[int, int_]) -> None:
    """Exits the program with the given status."""
    if isinstance(status, int_):
        status = status.value
    if not isinstance(status, int):
        raise TypeError("status must be an int.")
    exit(status) # Let python do the work

def _Exit(status:Union[int, int_]) -> None:
    """Exits the program with the given status."""
    if isinstance(status, int_):
        status = status.value
    if not isinstance(status, int):
        raise TypeError("status must be an int.")
    exit(status) # Let python do the work

def atexit(func:Callable) -> None:
    """Registers a function to be called at program exit."""
    pass # TODO: Implement

malloc = _mmodc.malloc
calloc = _mmodc.calloc
realloc = _mmodc.realloc
free = _mmodc.free

def atoi(nptr:Union[_mmodc.CHAR_PTR, str]) -> int_: # when making c funcs use c types
    """Converts a string to an integer."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)
    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    return int_(nptr)

def atol(nptr:Union[_mmodc.CHAR_PTR, str]) -> long:
    """Converts a string to a long."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)
    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    return long(nptr)

def atoll(nptr:Union[_mmodc.CHAR_PTR, str]) -> long_long:
    """Converts a string to a long long."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)
    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    return long_long(nptr)

def strtol(nptr:Union[_mmodc.CHAR_PTR, str], endptr:_mmodc.Pointer[_mmodc.CHAR_PTR], base:Union[int, int_]) -> long:
    """Converts a string to a long."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)

    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    if isinstance(base, int_):
        base = base.value

    if not isinstance(base, int):
        raise TypeError("base must be an int.")

    if not isinstance(endptr, _mmodc.Pointer):
        raise TypeError("endptr must be a char**.")

    pass # TODO: Implement

def strtoll(nptr:Union[_mmodc.CHAR_PTR, str], endptr:_mmodc.Pointer[_mmodc.CHAR_PTR], base:Union[int, int_]) -> long_long:
    """Converts a string to a long long."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)

    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    if isinstance(base, int_):
        base = base.value

    if not isinstance(base, int):
        raise TypeError("base must be an int.")

    if not isinstance(endptr, _mmodc.Pointer):
        raise TypeError("endptr must be a char**.")

    pass # TODO: Implement

def stroul(nptr:Union[_mmodc.CHAR_PTR, str], endptr:_mmodc.Pointer[_mmodc.CHAR_PTR], base:Union[int, int_]) -> unsigned_long:
    """Converts a string to an unsigned long."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)

    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    if isinstance(base, int_):
        base = base.value

    if not isinstance(base, int):
        raise TypeError("base must be an int.")

    if not isinstance(endptr, _mmodc.Pointer):
        raise TypeError("endptr must be a char**.")

    pass # TODO: Implement

def strtod(nptr:Union[_mmodc.CHAR_PTR, str], endptr:_mmodc.Pointer[_mmodc.CHAR_PTR]) -> float:
    """Converts a string to a double."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)

    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    if not isinstance(endptr, _mmodc.Pointer):
        raise TypeError("endptr must be a char**.")

    pass # TODO: Implement

def strtold(nptr:Union[_mmodc.CHAR_PTR, str], endptr:_mmodc.Pointer[_mmodc.CHAR_PTR]) -> long_double:
    """Converts a string to a long double."""
    if isinstance(nptr, _mmodc.Pointer):
        nptr = _mmodc.get_string(nptr)

    if not isinstance(nptr, str):
        raise TypeError("nptr must be a char*")

    if not isinstance(endptr, _mmodc.Pointer):
        raise TypeError("endptr must be a char**.")

    pass # TODO: Implement

def rand() -> int_:
    """Returns a random number."""
    from random import randint
    return int_(randint(0, RAND_MAX))

def srand(seed:Union[unsigned_int, int]) -> None:
    """Sets the seed for the random number generator."""
    if isinstance(seed, unsigned_int):
        seed = seed.value

    if not isinstance(seed, int):
        raise TypeError("seed must be an uint.")

    pass # TODO: Implement

def abs(x:Union[int, int_]) -> int_:
    """Returns the absolute value of x."""
    if isinstance(x, int_):
        x = x.value

    if not isinstance(x, int):
        raise TypeError("x must be an int.")

    return int_(int(math.fabs(x)))

def labs(x:Union[long, int]) -> long:
    """Returns the absolute value of x."""
    if isinstance(x, int):
        x = long(x)

    if not isinstance(x, long):
        raise TypeError("x must be a long.")

    return long(int(math.fabs(x)))

def llabs(x:Union[long_long, int]) -> long_long:
    """Returns the absolute value of x."""
    if isinstance(x, int):
        x = long_long(x)

    if not isinstance(x, long_long):
        raise TypeError("x must be a long long.")

    return long_long(int(math.fabs(x)))
# Basic Needs
from phardwareitk_c import *
from phardwareitk.Extensions import C as _mmodc
# C libs
from phardwareitk_c.stdint import *
from phardwareitk_c.stddef import *

size_t = size_t # Well idk why but the real stdlib also does this.
wchar_t = wchar_t # again idk why but the real stdlib also does this.

div_t = _mmodc.Struct({
    "quot": {"type": _int, "value": None},
    "rem": {"type": _int, "value": None}
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

def _exit(status:int)
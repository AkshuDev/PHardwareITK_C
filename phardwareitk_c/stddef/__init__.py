# Basic needs
import phardwareitk.Extensions.C as _mmodc
from phardwareitk_c import *

# C libs
from phardwareitk_c.stdint import *

# Modules for fellow VSCode/IDE devs
from typing import *
# For arch detection
import platform

size_t = uint32_t
ptrdiff_t = int32_t
wchar_t = int32_t

if platform.architecture()[0] == "64bit":
    size_t = uint64_t
    ptrdiff_t = int64_t

if platform.system() == "Windows":
    wchar = uint16_t

max_align_t = _mmodc.Struct({"ll": {"type": long_long, "value": None}, "ld": {"type": long_double, "value": None}})

# Macros
NULL = _mmodc.Pointer(int, 0).cast(_mmodc.Void) # ((void*)0)

# Macro like funcs
def offsetof(type_:_mmodc.Struct, member:str) -> int:
    """Gets the offset of a member in a struct."""
    ptr = _mmodc.Pointer(int, 0)
    ptr.cast(type_)
    ptr_def:_mmodc.Struct = ptr.dereference()
    member_def = ptr_def.access(member)
    ptr_member = _mmodc.Pointer(int, member_def.address)
    return ptr_member.cast(size_t)



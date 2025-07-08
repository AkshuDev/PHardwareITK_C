# Main needs
from phardwareitk_c import *
from phardwareitk.Extensions import C as _mmodc

# For the people with VSCode or such IDE
from typing import *

# For arch detection
import platform

# Helper function
def initialize_memory(size:int, debug:bool=False) -> None:
	"""Initializes the memory"""
	_mmodc.reset_mem(size, debug)
	return

def reset_memory(size:int, debug:bool=False) -> None:
	"""Resets the entire memory using the size"""
	initialize_memory(size, debug)

initalized:bool = False

# Uint
class uint8_t(_mmodc.Uint8_t):
	"""Unsigned Integer of size 8 bits [uint8_t]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class uint16_t(_mmodc.Uint16_t):
	"""Unsigned Integer of size 16 bits [uint16_t]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class uint32_t(_mmodc.Uint32_t):
	"""Unsigned Integer of size 32 bits [uint32_t]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class uint64_t(_mmodc.Uint64_t):
	"""Unsigned Integer of size 64 bits [uint64_t]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class uint:
    pass

if platform.architecture()[0] == "64bit":
	class uint(uint64_t):
		"""Unsigned Integer of size 64 bits [uint]"""
		def __init__(value:Union[int, str, bytes]) -> None:
			super().__init__(value)

		def __repr__() -> str:
			return super().__repr__()

		def __del__() -> None:
			super().__del__()
else:
	class uint(uint32_t):
		"""Unsigned Integer of size 32 bits [uint]"""
		def __init__(value:Union[int, str, bytes]) -> None:
			super().__init__(value)

		def __repr__() -> str:
			return super().__repr__()

		def __del__() -> None:
			super().__del__()

# Int
class int8_t(_mmodc.Int8):
	"""Signed Integer of size 8 bits [int8]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class int16_t(_mmodc.Int16):
	"""Signed Integer of size 16 bits [int16]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class int32_t(_mmodc.Int32):
	"""Signed Integer of size 32 bits [int32]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class int64_t(_mmodc.Int64):
	"""Signed Integer of size 64 bits [int64]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()

class int_:
    pass

if platform.architecture()[0] == "64bit":
	class int_(int64_t):
		"""Signed Integer of size 64 bits [int]"""
		def __init__(value:Union[int, str, bytes]) -> None:
			super().__init__(value)

		def __repr__() -> str:
			return super().__repr__()

		def __del__() -> None:
			super().__del__()
else:
	class int_(int32_t):
		"""Signed Integer of size 32 bits [int]"""
		def __init__(value:Union[int, str, bytes]) -> None:
			super().__init__(value)

		def __repr__() -> str:
			return super().__repr__()

		def __del__() -> None:
			super().__del__()

# Least (typedefs)
uint_least8_t = uint8_t
int_least8_t = int8_t

# Fast
int_fast8_t = int_
int_fast16_t = int_
int_fast32_t = int32_t
int_fast64_t = int64_t
uint_fast8_t = uint
uint_fast16_t = uint
uint_fast32_t = uint32_t
uint_fast64_t = uint64_t

# Max
intmax_t = int64_t
uintmax_t = uint64_t

# Other types
char = int8_t
short = int16_t
long = int32_t # following the C standard

long_long = int64_t # ensures a consistent type of 64 bits
long_double = double # type alias for double

unsigned_long = uint64_t # type alias for unsigned long

unsigned_long_long = uint64_t # type alias for unsigned long long

unsigned_short = uint16_t
unsigned_char = uint8_t # type alias for unsigned char

unsigned_int = uint

# MACROS
# Bit widths (standard)
INT8_WIDTH = 8
INT16_WIDTH = 16
INT32_WIDTH = 32
INT64_WIDTH = 64

# Max Values for unsigned types
UINT8_MAX = 0xFF
UINT16_MAX = 0xFFFF
UINT32_MAX = 0xFFFFFFFF
UINT64_MAX = 0xFFFFFFFFFFFFFFFF

# Max Values for signed types
INT8_MAX = 0x7F
INT16_MAX = 0x7FFF
INT32_MAX = 0x7FFFFFFF
INT64_MAX = 0x7FFFFFFFFFFFFFFF

# Min Values for signed types
INT8_MIN = -128
IN16_MIN = -32768
INT32_MIN = -2147483648
INT64_MIN = -9223372036854775808

# Max values for pointer types
INTPTR_MIN = INT32_MIN

# Min values for pointer types
UINTPTR_MAX = UINT64_MAX
INTPTR_MAX = INT32_MAX

class intptr(int32_t):
	"""An signed Pointer with size of 4 bytes / 32 bits"""
	def __init__(self, type:object, object_:Union[object, int]) -> None:
		self.type = type
		self.pointer_address = None

		if isinstance(object_, int):
			self.pointer_address = object_
		elif object_ is None:
			pass
		else:
			if getattr(object_, "address", None) is None:
				raise TypeError("Can't use non C-Extension Type in a C-Extension module file")
			self.pointer_address = object_.address

		super().__init__(self.pointer_address)

	def cast(self, new_type:object) -> None:
		"""Casts the pointer to a new type"""
		self.type = new_type

	def dereference(self) -> Any:
		"""Dereferences the pointer"""
		if isinstance(self.type, _mmodc.Char):
			return _mmodc.get_string(self)

		size = _mmodc.get_size_metadata(self.pointer_address - 8)
		return _mmodc.get_mem(self.pointer_address, size)

	def __repr__(self) -> str:
		return f"*{self.pointer_address}"

	def __del__() -> None:
		super().__del__()

class uintptr(uint64_t):
	"""An Unsigned pointer of size 64 bits / 8 bytes"""
	def __init__(self, type:object, object_:Union[object, int]) -> None:
		self.type = type
		self.pointer_address = None

		if isinstance(object_, int):
			self.pointer_address = object_
		elif object_ is None:
			pass
		else:
			if getattr(object_, "address", None) is None:
				raise TypeError("Can't use non C-Extension Type in a C-Extension module file")
			self.pointer_address = object_.address

		super().__init__(self.pointer_address)

	def cast(self, new_type:object) -> None:
		"""Casts the pointer to a new type"""
		self.type = new_type

	def dereference(self) -> Any:
		"""Dereferences the pointer"""
		if isinstance(self.type, _mmodc.Char):
			return _mmodc.get_string(self)

		size = _mmodc.get_size_metadata(self.pointer_address - 8)
		return _mmodc.get_mem(self.pointer_address, size)

	def __repr__(self) -> str:
		return f"*{self.pointer_address}"

	def __del__() -> None:
		super().__del__()


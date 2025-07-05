# Main needs
from phardwareitk.Extensions import C as _mmodc

# For the people with VSCode or such IDE
from typing import *

# Helper function
def initialize_memory(size:int, debug:bool=False) -> None:
	"""Initializes the memory"""
	_mmodc.reset_mem(size, debug)
	return

def reset_memory(size:int, debug:bool=False) -> None:
	"""Resets the entire memory using the size"""
	initalize_memory(size, debug)

initalized:bool = False

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



class int8(_mmodc.Int8):
	"""Signed Integer of size 8 bits [int8]"""
	def __init__(value:Union[int, str, bytes]) -> None:
		super().__init__(value)

	def __repr__() -> str:
		return super().__repr__()

	def __del__() -> None:
		super().__del__()


class int16(_mmodc.Int16):
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

	def cast(new_type:object) -> None:
		"""Casts the pointer to a new type"""
		self.type = new_type

	def dereference() -> Any:
		"""Dereferences the pointer"""
		if isinstance(self.type, _mmodc.Char):
			return _mmodc.get_string(self)

		size = _mmodc.get_size_metadata(self.pointer_address - 8)
		return _mmodc.get_mem(self.pointer_address, size)

	def __repr__() -> str:
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

	def cast(new_type:object) -> None:
		"""Casts the pointer to a new type"""
		self.type = new_type

	def dereference() -> Any:
		"""Dereferences the pointer"""
		if isinstance(self.type, _mmodc.Char):
			return _mmodc.get_string(self)

		size = _mmodc.get_size_metadata(self.pointer_address - 8)
		return _mmodc.get_mem(self.pointer_address, size)

	def __repr__() -> str:
		return f"*{self.pointer_address}"

	def __del__() -> None:
		super().__del__() 


"""Basic pre-build C types for C (they are also in C but not defined in any lib/headers)"""
from phardwareitk.Extensions import C as _mmodc

class double(float):
    """Double precision floating point number [double]"""
    def __init__(self, value: float) -> None:
        self.size = 8
        self.value = value
        self.address = _mmodc.get_next_alloc()
        _mmodc.append_next_alloc(self.size)
        _mmodc.set_mem(self.address, self.value, self.size)
        super().__init__(value)

    def __repr__(self) -> str:
        return super().__repr__()

    def __del__(self) -> None:
        _mmodc.del_mem(self.address, self.size)
        super().__del__()



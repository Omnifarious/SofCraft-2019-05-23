from __future__ import annotations


class FizzBuzzer(object):
    def __init__(self, n: int, *args, **kargs):
        super().__init__(*args, **kargs)
        self.n_: int = n

    def __eq__(self, other: FizzBuzzer) -> bool:
        return ((self.n_ % 3 == 0) and (other.n_ % 3 == 0)) or \
               ((self.n_ % 5 == 0) and (other.n_ % 5 == 0)) or \
               self.n_ == other.n_

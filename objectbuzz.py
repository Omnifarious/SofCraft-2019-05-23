from __future__ import annotations


class FizzBuzzer(object):
    def __init__(self, n: int, *args, **kargs):
        super().__init__(*args, **kargs)
        self.n_: int = n

    def __eq__(self, other: FizzBuzzer) -> bool:
        return (self.n_ == other.n_) or \
               ((5 * (((self.n_ % 3 == 0) and 1) + ((self.n_ % 5 == 0) and 2))) -
                (((other.n_ % 3 == 0) and 1) + ((other.n_ % 5 == 0) and 2))) in (4, 8, 12)

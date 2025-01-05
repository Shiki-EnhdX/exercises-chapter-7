from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    symbol = "S"

    def _validate(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError("Value must be of type numpy.ndarray,"
                             f" not a {type(value).__name__}")
        if not (len(value) == self.n
                and sorted(value) == [i for i in range(self.n)]):
            raise ValueError("Value must be a rearrangement "
                             f"of the integers from 0 to {self.n}")

    def operation(self, a, b):
        return a[b]

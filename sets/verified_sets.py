from numbers import Integral


class UniquenessError(KeyError):
    pass


class VerifiedSet(set):
    def __init__(self, input=None):
        if input:
            for elem in input:
                self._verify(elem)
            super().__init__(input)
        else:
            super().__init__()

    def _verify(self, elem):
        raise NotImplementedError

    def add(self, elem):
        self._verify(elem)
        super().add(elem)

    def update(self, other):
        for elem in other:
            self._verify(elem)
        super().update(other)

    def symmetric_difference_update(self, other):
        for elem in other:
            self._verify(elem)
        super().symmetric_difference_update(other)

    def union(self, other):
        for elem in other:
            self._verify(elem)
        return type(self)(super().union(other))

    def intersection(self, other):
        for elem in other:
            self._verify(elem)
        return type(self)(super().intersection(other))

    def difference(self, other):
        for elem in other:
            self._verify(elem)
        return type(self)(super().difference(other))

    def symmetric_difference(self, other):
        for elem in other:
            self._verify(elem)
        return type(self)(super().symmetric_difference(other))

    def copy(self):
        return type(self)(super().copy())


class IntSet(VerifiedSet):
    def _verify(self, elem):
        if not isinstance(elem, Integral):
            raise TypeError("IntSet expected an integer,"
                            f" got a {type(elem).__name__}.")


class UniqueSet(VerifiedSet):
    def _verify(self, elem):
        if elem in self:
            raise UniquenessError

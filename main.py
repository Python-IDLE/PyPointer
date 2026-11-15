
class Cell:
    """A mutable container for otherwise immutable values."""

    def __init__(self, value):
        self.value = value


class Pointer:
    def __init__(self, target=None, index=None, key=None, attribute=None):
        self.target = target
        self.index = index
        self.key = key
        self.attribute = attribute

    @classmethod
    def null(cls):
        return cls()

    def is_null(self):
        return self.target is None

    @property
    def value(self):
        if self.is_null():
            raise ReferenceError("Null pointer")

        if isinstance(self.target, Cell):
            if self.index is None:
                return self.target.value
            return self.target.value[self.index]

        if self.index is not None:
            return self.target[self.index]

        if self.key is not None:
            return self.target[self.key]

        if self.attribute is not None:
            return getattr(self.target, self.attribute)

        raise TypeError("Unsupported pointer target")

    @value.setter
    def value(self, new_value):
        if self.is_null():
            raise ReferenceError("Null pointer")

        if isinstance(self.target, Cell):
            if self.index is None:
                self.target.value = new_value
            else:
                data = self.target.value
                if isinstance(data, str):
                    data = list(data)
                    data[self.index] = new_value
                    self.target.value = "".join(data)
                else:
                    data[self.index] = new_value
            return

        if self.index is not None:
            self.target[self.index] = new_value
        elif self.key is not None:
            self.target[self.key] = new_value
        elif self.attribute is not None:
            setattr(self.target, self.attribute, new_value)
        else:
            raise TypeError("Unsupported pointer target")


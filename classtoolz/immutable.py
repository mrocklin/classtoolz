from classtoolz.core import Base

class Immutable(Base):
    """ Immutability class Mixin

    Supports only a single write, ideally at object creation time

    >>> class Person(Immutable):
    ...     def __init__(self, name, age):
    ...         self.name = name
    ...         self.age = age

    >>> Alice = Person('Alice', 25)
    >>> Alice.age = 26
    Traceback (most recent call last):
        ...
    TypeError: Person class is immutable
    """
    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            if value == getattr(self, attr):
                return value
            else:
                raise TypeError("%s class is immutable" % type(self).__name__)
        else:
            super(Immutable, self).__setattr__(attr, value)

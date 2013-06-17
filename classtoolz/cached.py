from classtoolz.core import Base

class Cached(Base):
    """ Cached class Mixin

    >>> class Person(Cached): pass

    >>> Person('Alice', 25) is Person('Alice', 25)
    True
    """
    _cache = dict()

    @staticmethod
    def _key(cls, *args, **kwargs):
        return (cls, args, frozenset(kwargs.items()))

    def __new__(cls, *args, **kwargs):
        key = Cached._key(cls, *args, **kwargs)
        if key not in Cached._cache:
            obj = object.__new__(cls)
            Cached._cache[key] = obj
        else:
            obj = Cached._cache[key]
        return obj

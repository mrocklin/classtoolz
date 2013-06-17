# http://stackoverflow.com/questions/8972866/correct-way-to-use-super-argument-passing
class Base(object):
    def __init__(self, *args, **kwargs): pass


class Slotted(Base):
    """ Boilerplate for standard Python class

    >>> class Person(Slotted):
    ...     __slots__ = ['name', 'age']

    >>> p = Person('Alice', 25)
    >>> p.name
    'Alice'
    >>> p.age
    25
    """

    def __init__(self, *args, **kwargs):
        try:
            for slot, arg in zip(self.__slots__, args):
                setattr(self, slot, arg)
        except AttributeError:
            raise TypeError("%s does not define __slots__" %
                             type(self).__name__)
        super(Slotted, self).__init__(*args, **kwargs)

    def _info(self):
        return (type(self), tuple(map(self.__getattribute__, self.__slots__)))

    def __eq__(self, other):
        return self._info() == other._info()

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,
               ', '.join("%s=%s" % (slot, getattr(self, slot))
                            for slot in self.__slots__))

    __repr__ = __str__


class Typed(Base):
    """ Type checking Mixin

    >>> class Person(Typed):
    ...     __types__ = [str, int]

    >>> Alice = Person('Alice', 25)
    >>> Bob = Person('Bob', 22.5)
    Traceback (most recent call last):
        ...
    TypeError: 22.5 should be of type int. Got type float


    """
    def __init__(self, *args, **kwargs):
        try:
            for typ, arg in zip(self.__types__, args):
                if not isinstance(arg, typ):
                    raise TypeError('%s should be of type %s. Got type %s'
                                         % (arg, typ.__name__, type(arg).__name__))
        except AttributeError:
            if not hasattr(self, '__types__'):
                raise TypeError("%s does not define __types__" %
                        type(self).__name__)
        super(Typed, self).__init__(*args, **kwargs)


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


class Person(Slotted, Typed, Immutable, Cached):
    """ A Person class

    Example for Slotted, Typed, Immutable and Cached mixins

    >>> Alice = Person('Alice', 25)
    >>> Alice
    Person(name=Alice, age=25)

    >>> Alice.age = 26
    Traceback (most recent call last):
        ...
    TypeError: Person class is immutable

    >>> Bob = Person('Bob', 22.5)
    Traceback (most recent call last):
        ...
    TypeError: 22.5 should be of type int. Got type float

    >>> Alice2 = Person('Alice', 25)  # A duplicate
    >>> Alice is Alice2
    True

    """
    __slots__ = ['name', 'age']
    __types__ = [str, int]

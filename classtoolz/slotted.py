from classtoolz.core import Base

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

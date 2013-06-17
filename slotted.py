# http://stackoverflow.com/questions/8972866/correct-way-to-use-super-argument-passing
class Base(object):
    def __init__(self, *args, **kwargs): pass


class Slotted(Base):
    """ Boilerplate for standard Python class

    >>> class Account(Slotted):
    ...     __slots__ = ['first', 'last', 'id', 'balance']
    ...
    ...     def name(self):
    ...         return "%s %s" (self.first, self.last)
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
    ...     def __init__(self, name, age):
    ...         super(Person, self).__init__(name, age)
    ...         self.name = name
    ...         self.age = age

    >>> Alice = Person('Alice', 25)
    >>> Bob = Person('Bob', 'Jones')
    TypeError()

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

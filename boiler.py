class Boiler(object):
    """ Boilerplate for standard Python class

    >>> class Account(Boiler):
    ...     __slots__ = ['first', 'last', 'id', 'balance']
    ...
    ...     def name(self):
    ...         return "%s %s" (self.first, self.last)
    """

    def __init__(self, *args):
        try:
            for slot, arg in zip(self.__slots__, args):
                setattr(self, slot, arg)
        except AttributeError:
            raise TypeError("%s does not define __slots__" %
                             type(self).__name__)

    def _info(self):
        return (type(self), tuple(map(self.__getattribute__, self.__slots__)))

    def __eq__(self, other):
        return self._info() == other._info()

    def __str__(self):
        return ('%s -- ' % type(self).__name__
              + ', '.join("%s: %s" % (slot, getattr(self, slot))
                            for slot in self.__slots__))

    __repr__ = __str__

class TypedBoiler(Boiler):
    """ Boilerplate for standard Python class

    >>> class Account(TypedBoiler):
    ...     __slots__ = ['first', 'last', 'id', 'balance']
    ...     __types__ = [str, str, int, int]
    ...
    ...     def name(self):
    ...         return "%s %s" (self.first, self.last)
    """
    def __init__(self, *args):
        try:
            for slot, typ, arg in zip(self.__slots__, self.__types__, args):
                if not isinstance(arg, typ):
                    raise TypeError('%s should be of type %s. Got type %s'
                                     % (arg, typ.__name__, type(arg).__name__))
                setattr(self, slot, arg)
        except AttributeError:
            if not hasattr(self, '__slots__'):
                raise TypeError("%s does not define __slots__" %
                        type(self).__name__)
            if not hasattr(self, '__types__'):
                raise TypeError("%s does not define __types__" %
                        type(self).__name__)

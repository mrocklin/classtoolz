class Boiler(object):
    """ Boilerplate for standard Python class

    >>> class Account(Boiler):
    ...     __slots__ = ['first', 'last', 'id', 'balance']
    ...     __types__ = [str, str, int, int]
    ...
    ...     def name(self):
    ...         return "%s %s" (self.first, self.last)
    """

    def __init__(self, *args):
        if hasattr(self, '__types__'):
            for typ, arg in zip(self.__types__, args):
                if not isinstance(arg, typ):
                    raise TypeError('%s should be of type %s. Got type %s'
                                     % (arg, typ.__name__, type(arg).__name__))
        try:
            for slot, arg in zip(self.__slots__, args):
                setattr(self, slot, arg)
        except AttributeError:
            raise TypeError("%s does not define __slots__" % type(self))

    def _info(self):
        return (type(self), tuple(map(self.__getattribute__, self.__slots__)))

    def __eq__(self, other):
        return self._info() == other._info()

    def __str__(self):
        return ('%s -- ' % type(self).__name__
              + ', '.join("%s: %s" % (slot, getattr(self, slot))
                            for slot in self.__slots__))

    __repr__ = __str__
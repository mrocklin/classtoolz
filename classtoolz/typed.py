from classtoolz.core import Base

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

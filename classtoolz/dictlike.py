from classtoolz.core import Base

class DictLike(Base, dict):
    """ Treat object like a dictionary

    >>> class Person(DictLike):
    ...     pass

    >>> p = Person()
    >>> p.name = "Alice"    # Can assign attributes to object as normal
    >>> p['age'] = 25       # Or using dictionary setitem syntax

    >>> p.age               # Can access these attributes as object attributes
    25
    >>> p['name']           # Or as key/value pairs
    'Alice'

    >>> list(sorted(p.keys()))      # Object acts in every way like a dict
    ['age', 'name']

    >>> p                           # doctest: +SKIP
    {'age': 25, 'name': 'Alice'}
    """
    def __init__(self, *args, **kwargs):
        super(DictLike, self).__init__(*args, **kwargs)

    def __setattr__(self, attr, value):
        self[attr] = value
        object.__setattr__(self, attr, value)
        return value

    def __getattr__(self, attr):
        return self[attr]


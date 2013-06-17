from classtoolz import Slotted, Typed, Immutable, Cached

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

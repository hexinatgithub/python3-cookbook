import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            # The operator.itemgetter() function creates an accessor function and the
            # property() function turns it into a property.
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']

# Unlike __init__(), the __new__() method gets triggered before an instance is created.
# Since tuples are immutable, it’s not possible to make any changes to them once they
# have been created. An __init__() function gets triggered too late in the instance cre‐
# ation process to do what we want. That’s why __new__() has been defined.

class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass


class MyMeta(type):

    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        return super().__prepare__(name, bases)

    # Required

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        return super().__new__(cls, name, bases, ns)

    # Required

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        super().__init__(name, bases, ns)

# Adding optional keyword arguments to a metaclass requires that you understand all of
# the steps involved in class creation, because the extra arguments are passed to every
# method involved. The __prepare__() method is called first and used to create the class
# namespace prior to the body of any class definition being processed. Normally, this
# method simply returns a dictionary or other mapping object. The __new__() method
# is used to instantiate the resulting type object. It is called after the class body has been
# fully executed. The __init__() method is called last and used to perform any additional
# initialization steps.
# When writing metaclasses, it is somewhat common to only define a __new__() or
# __init__() method, but not both. However, if extra keyword arguments are going to
# be accepted, then both methods must be provided and given compatible signatures. The
# default __prepare__() method accepts any set of keyword arguments, but ignores them.
# You only need to define it yourself if the extra arguments would somehow affect man‐
# agement of the class namespace creation.
# The use of keyword-only arguments in this recipe reflects the fact that such arguments
# will only be supplied by keyword during class creation.

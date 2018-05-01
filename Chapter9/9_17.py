from inspect import signature
import logging


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # find definitions located further up the class
        # hierarchy that make up the parents of self
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)


# Example

class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass


# A key feature of a metaclass is that it allows you to examine the contents of a class at the
# time of definition. Inside the redefined __init__() method, you are free to inspect the
# class dictionary, base classes, and more. Moreover, once a metaclass has been specified
# for a class, it gets inherited by all of the subclasses. Thus, a sneaky framework builder
# can specify a metaclass for one of the top-level classes in a large hierarchy and capture
# the definition of all classes under it.

# __new__() is invoked prior to class creation and
# is typically used when a metaclass wants to alter the class definition in some way (by
# changing the contents of the class dictionary). The __init__() method is invoked after
# a class has been created, and is useful if you want to write code that works with the fully
# formed class object.

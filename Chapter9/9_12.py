def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        # Make a new definition
        print('getting:', name)
        return orig_getattribute(self, name)
    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

# If you are applying multiple class decorators to a class, the application order might
# matter. For example, a decorator that replaces a method with an entirely new imple‐
# mentation would probably need to be applied before a decorator that simply wraps an
# existing method with some extra logic.

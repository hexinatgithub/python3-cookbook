# A proxy class that wraps around another object, but
# exposes its public attributes


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        # Delegate attribute lookup to internal obj
        # It is also important to emphasize that the __getattr__() method usually does not apply
        # to most special methods that start and end with double underscores.
        print('getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Delegate attribute assignment
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        # Delegate attribute deletion
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x)  # Outputs 2
p.bar(3)  # Outputs "Spam.bar: 2 3"
p.x = 37  # Changes s.x to 37

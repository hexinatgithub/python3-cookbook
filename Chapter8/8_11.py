class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            # Set the arguments (alternate)
            # If a subclass decided to use __slots__ or wrap a specific attribute with a
            # property (or descriptor), directly acccessing the instance dictionary would break.
            # setattr will call descriptor method, but below will not.
            # self.__dict__.update(zip(self._fields, args))


# Example class definitions
if __name__ == '__main__':
    import math

    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2


# support kwargs
# class Structure:
#     _fields = []

#     def __init__(self, *args, **kwargs):
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Set all of the positional arguments
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#         # Set the remaining keyword arguments
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#         # Check for any remaining unknown arguments
#         if kwargs:
#             raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

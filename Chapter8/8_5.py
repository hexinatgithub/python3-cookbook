class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self): 
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass

class B:
    def __init__(self):
        self.__private = 0
    
    # two leading underscores (__) on names cannot be overridden via inheritance.
    def __private_method(self):
        pass
    
    def public_method(self):
        self.__private_method()

# sometimes you may want to define a variable that clashes with the name of a reserved word. 
# For this, you should use a single trailing underscore.
lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword

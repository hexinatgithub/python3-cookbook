class Person:
    def __init__(self, name):
        self.name = name
    
    # Getter function
    @property
    def name(self): 
        return self._name
    
    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person): 
    @property
    def name(self): 
        print('Getting name') 
        return super().name
    
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
    
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

    # If you only want to redefine one of the methods, 
    # it’s not enough to use @property by itself.

    # @property # Doesn't work 
    # def name(self):
    #     print('Getting name')
    #     return super().name

    # If you don’t know which base class defined a property, 
    # you should use the solution where all of the property methods are redefined 
    # and super() is used to pass control to the previous implementation.
    # @Person.getter # Does work
    # def name(self): 
    #     print('Getting name')
    #     return super().name
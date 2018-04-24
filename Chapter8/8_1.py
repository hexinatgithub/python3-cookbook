class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self) 
        
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# The built-in repr() function returns this text, 
# as does the interactive interpreter when inspecting values. 
# The __str__() method converts the instance to a string, 
# and is the output produced by the str() and print() functions.

p = Pair(3, 4)
p # Pair(3, 4) Pair(3, 4)
print(p) # (3, 4) __str__() output

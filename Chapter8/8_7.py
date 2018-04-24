class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam') 
        super().spam()
        # Call parent spam()

class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value): 
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
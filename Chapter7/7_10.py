def apply_async(func, args, *, callback): 
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)

apply_async(add, ('hello', 'world'), callback=print_result)

# carry extra information in a callback

# bound-method
class ResultHandler: 
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)

# use a closure
def make_handler(): 
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)

# using an extra argument and partial function application
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))

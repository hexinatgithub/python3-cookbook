# 9.6. Defining a Decorator That Takes an Optional Argument
from functools import wraps, partial
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        if func is None:
            return partial(logged, level=level, name=name, message=message)

        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

# Example use
@logged
def add(x, y): 
    return x + y

@logged(level=logging.CRITICAL, name='example') 
def spam():
    print('Spam!')

"""
# Example use
@logged
def add(x, y): 
    return x + y

def add(x, y): 
    return x + y
add = logged(add)

@logged(level=logging.CRITICAL, name='example') 
def spam():
    print('Spam!')

def spam(): 
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)
"""
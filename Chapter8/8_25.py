# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
        return s

# When maintaining a cache of instances, you
# often only want to keep items in the cache as long as they’re actually being used some‐
# where in the program. A WeakValueDictionary instance only holds onto the referenced
# items as long as they exist somewhere else. Otherwise, the dictionary keys disappear
# when instances are no longer being used.


import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
            return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam.manager.get_spam(name)


# if you want to give users a stronger hint that they shouldn’t instantiate
# Spam instances directly, you can make __init__() raise an exception and use a class
# method to make an alternate constructor like this:
class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)  # Modified creation
            self._cache[name] = s
        else:
            s = self._cache[name]
            return s

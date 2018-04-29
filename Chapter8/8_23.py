import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root
print(c1.parent)


# Python’s garbage collection is based on simple reference count‐
# ing. When the reference count of an object reaches 0, it is immediately deleted. For
# cyclic data structures, however, this never happens. Thus, in the last part of the example,
# the parent and child nodes refer to each other, keeping the reference count nonzero.
# To deal with cycles, there is a separate garbage collector that runs periodically. However,
# as a general rule, you never know when it might run. Consequently, you never really
# know when cyclic data structures might get collected. If necessary, you can force garbage
# collection, but doing so is a bit clunky:
# import gc
# gc.collect() # Force collection

# !!!!!
# An even worse problem occurs if the objects involved in a cycle define their own
# __del__() method.

def spam(a, b, c, d): 
    print(a, b, c, d)

from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)
s2 = partial(spam, d=42)
s2(1, 2, 3)
s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
s3(3)

points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance,pt))
points

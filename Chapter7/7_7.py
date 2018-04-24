x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
a(10) # 20
b(10) # 30

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
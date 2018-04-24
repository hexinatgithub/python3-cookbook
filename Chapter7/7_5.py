x = 42
# The values assigned as a default are bound 
# only once at the time of function definition.
def spam(a, b=x): 
    print(a, b)

spam(1) # Ok. a=1, b=42 spam(1, 2) # Ok. a=1, b=2
x = 23
spam(1) # 1 42

# If you do this, you can run into all sorts of trouble 
# if the default value ever escapes the function and gets modified.
def spam(a, b=[]): # NO! ...
    pass
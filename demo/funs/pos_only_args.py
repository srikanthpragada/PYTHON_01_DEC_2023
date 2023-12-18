# positional-only args
def fun(x, y, /):
    pass


fun(10, 20)
#fun(b=1, a=2)

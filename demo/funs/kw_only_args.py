# kw-only args
def fun(*, b, a):
    pass


# fun(10, 20)
fun(a=1, b=2)
fun(b=1, a=2)

# Overloading

def add(a, b):
    return a + b


add2 = add
print(type(add2))


def add(a, b, c):
    return a + b + c


print(add2(10, 20))
print(add(10, 20, 30))

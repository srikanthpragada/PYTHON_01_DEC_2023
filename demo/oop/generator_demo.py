def numbers():
    for n in range(1, 4):
        yield n


g = numbers()

print(type(g))

print(next(g))
print(next(g))
print(next(g))

ge = (n for n in range(1, 10000))  # lazy
lc = [n for n in range(1, 10000)]  # eager

print(type(ge))
print(next(ge))

import sys

print(sys.getsizeof(ge), sys.getsizeof(lc))

# prime(100,200)
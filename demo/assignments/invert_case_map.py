def invert(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()


# print(invert('a'), invert('L'), invert('9'))

for c in map(invert, "AbcXy23Pq"):
    print(c, end='')
   
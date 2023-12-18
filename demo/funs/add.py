def add(a, b):
    return a + b


def iseven(n):
    return n % 2 == 0


def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


print(add(10, 20))
print(iseven(11), iseven(12))
print(count_upper('AbCD'))

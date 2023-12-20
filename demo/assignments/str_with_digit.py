data = ['Abc', 'A12', 'X3', 'DEF', '999']


def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


for n in filter(hasdigit, data):
    print(n)


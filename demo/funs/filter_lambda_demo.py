nums = [11, 12, 44, 56, 77, 99]

for n in filter(lambda v: v % 2 == 0, nums):
    print(n)

for s in filter(lambda s: len(s) > 4, ['Scott', 'Joe', 'Mark', 'David']):
    print(s)

def iseven(n):
    return n % 2 == 0


nums = [11, 12, 44, 56, 77, 99]

for n in filter(iseven, nums):
    print(n)

# Select all uppercase letters
for c in filter(str.isupper, 'This is Fine'):
    print(c)


def bignames(s):
    return len(s) > 4


for s in filter(bignames, ['Scott', 'Joe', 'Mark', 'David']):
    print(s)

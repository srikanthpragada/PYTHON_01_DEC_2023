names = ['Java', 'Python', 'C#', 'JavaScript']

for n in map(len, names):
    print(n)

nums = ['10', '20', '45']

print(sum(map(int, nums)))


def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


for c in map(count_digits, ['A123', 'BB45', 'C5', "DE"]):
    print(c)

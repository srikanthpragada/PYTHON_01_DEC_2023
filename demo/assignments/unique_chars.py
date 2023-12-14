
chars = set()

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    chars = chars | set(name)

print(sorted(chars))

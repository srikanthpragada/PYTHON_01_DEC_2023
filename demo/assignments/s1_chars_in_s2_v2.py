s1 = "abcdefc"
s2 = "efxyzc"

chars = []
for c in s1:
    if c in s2:
        if c not in chars:
            print(c)
            chars.append(c)


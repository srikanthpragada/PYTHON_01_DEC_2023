import re

with open("test.txt", "rt") as f:
    contents = f.read()

# Replace multiple spaces with one space

contents = re.sub(' +', ' ', contents)
contents = re.sub('\n+', '\n', contents)

with open("test.txt", "wt") as f:
    f.write(contents)

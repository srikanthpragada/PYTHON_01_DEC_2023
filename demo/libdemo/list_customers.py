import re

f = open("customers.txt", "rt")

for line in f.readlines():
    # take customer name
    m = re.search('[A-Za-z ]+', line)
    if m is None:  # name not found
        continue

    name = m.group().strip()

    m = re.search('[0-9]+', line)
    if m is None:  # mobile not found
        continue

    mobile = m.group()

    print(f"{name:20} {mobile:10}")

f.close()

def getsum(data):
    total = 0
    for e in data:
        if e.strip().isdigit():
            total += int(e)

    return total


f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.split(",")

    if len(parts) < 2:  # not enough data
        continue

    name = parts[0]
    marks = parts[1:]
    # total = sum(map(int, marks))
    total = getsum(marks)

    print(f"{name:20} {total:3}")

f.close()

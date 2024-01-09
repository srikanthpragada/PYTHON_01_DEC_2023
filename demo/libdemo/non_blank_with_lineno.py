filename = input("Enter filename : ")

f = open(filename, "rt")

lines = []
for line in f.readlines():
    if len(line.strip()) > 0:  # non-blank line
        lines.append(line.strip())

f.close()

for line in sorted(lines):
    print(line)


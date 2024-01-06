
f = open("names.txt", "wt")

names = ['Java', "JavaScript", "Python", 'C#', 'SQL']

for n in names:
    f.write(n + "\n")

f.close()


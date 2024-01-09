import os

allfiles = os.walk(r"d:\classroom\dec1\demo")

count = 0
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            count += 1
            print(dirname + "\\" + f)

print("Count = ", count)


total = 0
while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break
    if n < 0:
        continue

    total += n

print(total)


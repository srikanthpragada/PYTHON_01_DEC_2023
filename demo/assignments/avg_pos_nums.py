
total = 0
count = 0

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break
    if n < 0:
        continue

    total += n
    count += 1

print('Average =', total // count)


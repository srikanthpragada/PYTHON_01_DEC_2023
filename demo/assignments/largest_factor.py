# Display largest factor

num = int(input("Enter number :"))

for n in range(num // 2, 1, -1):
    if num % n == 0:
        print(n)
        break
else:
    print(1)  # for prime numbers



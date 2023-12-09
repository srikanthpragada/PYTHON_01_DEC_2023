# Display whether number is prime or not

num = int(input("Enter number :"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print('Not a prime number')
        break  # stop loop
else:
    print('Prime number')

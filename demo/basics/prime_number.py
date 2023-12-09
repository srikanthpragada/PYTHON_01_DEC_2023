# Display whether number is prime or not

num = int(input("Enter number :"))

prime = True
for n in range(2, num // 2 + 1):
    if num % n == 0:
        print('Not a prime')
        prime = False
        break  # stop loop

if prime:
    print('Prime number')



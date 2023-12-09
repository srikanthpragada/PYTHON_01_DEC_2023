# Sum of digits

num = int(input("Enter number :"))

total = 0
while num > 0:
    digit = num % 10
    total += digit   # total = total + digit
    num //= 10      # num = num // 10

print(total)
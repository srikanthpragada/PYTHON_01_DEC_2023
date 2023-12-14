nums = set()  # empty set
while True:
    num = int(input("Enter the num (o to stop) :"))
    if num == 0:
        break

    nums.add(num)

print(sorted(nums))

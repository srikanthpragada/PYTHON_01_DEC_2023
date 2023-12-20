data = "10,40,50,60"
nums = data.split(",")
print(nums)

total = sum(map(int, nums))
avg = total / len(nums)
print(avg)

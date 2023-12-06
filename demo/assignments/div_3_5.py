# Check whether num is divisible by 3 and 5

num = int(input("Enter number :"))

if num % 3 == 0 and num % 5 == 0:
    print("Both")
elif num % 3 == 0:
    print("3")
elif num % 5 == 0:
    print("5")
else:
    print("None")




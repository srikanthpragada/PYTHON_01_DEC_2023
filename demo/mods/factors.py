# Display factors for the given number other than
# 1 and itself

import sys

if len(sys.argv) < 2:
    print('Missing number. Please provide number on command-line!')
    exit()

num = int(sys.argv[1])  # Take command-line argument

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n, end=' ')


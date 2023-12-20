names = ['Jackson', 'Joe', 'Andy', 'Larry', 'Malcolm', 'Li'];

for n in sorted(names, key=len):
    print(n)

nums = [-10, 5, 6, 90, -100, -30, 50];

for n in sorted(nums, key=abs):
    print(n)

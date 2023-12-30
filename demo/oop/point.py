class Point:
    pass


p1 = Point()
p1.x = 10
print(p1.__dict__)

print(getattr(p1, 'x'))
print(getattr(p1, 'y', 10))

print(hasattr(p1, 'y'))
setattr(p1, 'y', 100)
print(hasattr(p1, 'y'))
delattr(p1, 'y')
print(hasattr(p1, 'y'))


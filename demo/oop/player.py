class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    # Convert player to int
    def __int__(self):
        return self.age


p1 = Player("Ronaldo", 37)
p2 = Player("Ronaldo", 37)
p3 = Player("Dhoni", 40)

print(p1)  # p1.__str__()
print(str(p1))  # p1.__str__()

print(p1 == p2)  # p1.__eq__(p2)
print(p1 != p3)  # p1.__eq__(p3)

print(p1 > p3)  # p1.__gt__(p3)
print(p1 < p3)  # p1.__gt__(p3)

v = int(p1)  # p1.__int__()

players = [Player("First", 20),
           Player("Second", 40),
           Player("Third", 25)]

for p in sorted(players, key=lambda p: p.name):
    print(p)

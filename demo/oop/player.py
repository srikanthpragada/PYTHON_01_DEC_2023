class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"


p1 = Player("Ronaldo", 37)
p2 = Player("Ronaldo", 37)
p3 = Player("Dhoni", 40)

print(p1)  # p1.__str__()
print(str(p1))  # p1.__str__()

print(p1 == p2)  # p1.__eq__(p2)




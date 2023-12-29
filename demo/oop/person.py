class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


p1 = Person("Jack", "99292922")
print(p1.name, p1.mobile)
p1.mobile = "393939393"


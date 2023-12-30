class Person:
    def __init__(self, name, mobile):
        self.name = name
        # private member
        self.__mobile = mobile



p1 = Person("Jack", "99292922")
print(p1.__dict__)

#p1.mobile = "393939393"
print(p1.name, p1._Person__mobile)


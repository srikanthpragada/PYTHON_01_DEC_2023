class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


import json

p = Person("Jack", "jack@gmail.com")
print(json.dumps(p.__dict__))


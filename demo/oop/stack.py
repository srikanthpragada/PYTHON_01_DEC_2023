class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            raise Exception('Stack is empty!')

        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def clear(self):
        self.data.clear()

    @property
    def length(self):
        return len(self.data)


s = Stack()
s.push(10)
s.push(20)
print(s.pop())
print(s.length)

for v in s:
    print(v)

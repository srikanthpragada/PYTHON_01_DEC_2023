def wish(*names, message="Hi"):
    for name in names:
        print(message, name)


wish('Larry', 'Scott', 'Joe')
wish('Mark', 'Jack', message='Hello')
wish('Mark', 'Jack', 'Hello')

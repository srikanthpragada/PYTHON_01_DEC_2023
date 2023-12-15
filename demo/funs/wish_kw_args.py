def wish(user, message):
    print(f"{message} {user}")


wish('Bill', 'Hi')  # positional
wish(message="Hello", user="Larry")  # keyword

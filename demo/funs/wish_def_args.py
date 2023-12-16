def wish(user='Guest', message='Hi'):
    print(f"{message} {user}")


wish('Bill', 'Hello')  # positional
wish(message="Hello", user="Larry")  # keyword
wish('Larry')
wish(message='Hello')
wish()

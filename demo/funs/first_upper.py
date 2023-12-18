
def first_upper(st):
    for c in st:
        if c.isupper():
            return c
        
    return None


print(first_upper("Hello"))
print(first_upper("hi"))

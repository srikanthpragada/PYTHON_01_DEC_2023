g = 100  # Global variable


# Enclosing function
def f1():
    global g
    a = 1  # Enclosing variable
    g = 200

    # Local function
    def f2():
        nonlocal a
        b = 10  # Local variable
        a = 1000
        print(g, a, b)

    f2()
    print(a)


f1()

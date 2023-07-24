x = 0


def a():
    x = 9

    def b():
        nonlocal x
        x += 1
        print(x)

    b()


a()
print(x)

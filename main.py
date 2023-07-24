x = 0


def a():
    x = 9

    def b():
        global x
        x += 1
        print(x)
    b()


a()

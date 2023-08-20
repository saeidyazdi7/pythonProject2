def star(func):
    def inner(*x, **y):
        print("x" * 20)
        func(*x, **y)
    return inner


@star
def msg(name):
    print("i am", name)


msg("Saeid")

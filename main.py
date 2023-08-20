from functools import wraps


def star(func):
    @wraps(func)
    def inner(*x, **y):
        print("x" * 20)
        func(*x, **y)

    return inner


@star
def msg(name):
    """Saeid jigili"""
    print("i am", name)


print(msg.__doc__)
print(msg.__name__)
msg("Saeid")

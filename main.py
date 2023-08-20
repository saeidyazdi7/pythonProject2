def dec(func):
    def inner(*x, **y):
        if y == 0:
            return "warning!"
        return func(*x, **y)

    return inner


@dec
def f(x, y, z):
    return x * y * z["A"]


print(f(5, 9, {"A": 2}))

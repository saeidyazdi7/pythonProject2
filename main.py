def func(x):
    print("saeid")
    yield x ** 2
    print("hallo")
    yield 5
    print("wie geht's?")
    yield x - 2


x = func(6)
print(next(x))
print(next(x))
print(next(x))

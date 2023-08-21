def fibo():
    f = 0
    yield f
    f1 = 1
    yield f1
    while True:
        f3 = f + f1
        yield f3
        f = f1
        f1 = f3


fib = fibo()
for _ in range(10):
    print(next(fib))

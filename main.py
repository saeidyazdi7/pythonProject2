def f(n):
    if n < 3:
        return
    elif n % 3 == 0:
        print(n)
    f(n - 1)


f(10)

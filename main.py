def func(x):
    return x ** 2


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = list(map(func, li))
print(new)

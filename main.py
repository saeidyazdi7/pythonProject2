def func(x):
    return x % 3


li = [1, 2, 3, 4, 9, 10, 28, 19]
new = sorted(li, key=func)
print(new)

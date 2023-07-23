def func(x: int, y: int = 9, **d: dict):
    return x, y, d


print(func(1, c=7, h=8))
print(func.__annotations__)

def func(x):
    if x % 2 != 0:
        return x
    else:
        return 0


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = [func(j) for j in x]
print(z)

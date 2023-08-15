def func(a):
    a[1] = 0
    print(a)


a = [1, 2, 3, 4, 5]
func(a[:])
print(a)

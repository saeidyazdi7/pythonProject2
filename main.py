def func(a, b=0, *c, **d):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


func(1, 2, 3, 4, 5, 6, 7, 8, c=50, y=100)

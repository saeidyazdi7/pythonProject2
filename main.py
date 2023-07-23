def func(a, b, c, /, d, e, *, f, g):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("e:", e)
    print("f:", f)
    print("g:", g)


func(1, 2, 3, 4, 5, f=50, g=100)

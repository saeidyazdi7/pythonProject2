def func(a, b=0, *c, **d):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


func(10,1,2,3,4,t="2")

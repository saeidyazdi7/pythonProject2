def func(a):
    print(a)

    def bunc(b):
        print(b ** 3)

    print(bunc.__name__)
    bunc(a)


func(2)
print(func.__name__)


x = 0


def A():
    x = 2
    print(x)

    def B():
        global x
        x = 3
        print(x)

    B()


A()
print(x)

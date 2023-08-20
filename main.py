def dec(fof):
    def inner():
        print("*")
        fof()
        print("*")

    return inner


@dec
def f():
    print("Saeid")
f()
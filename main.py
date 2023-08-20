def dec(fof):
    def inner():
        print("*")
        fof()
        print("*")

    return inner


def f():
    print("Saeid")


new_func = dec(f)
new_func()

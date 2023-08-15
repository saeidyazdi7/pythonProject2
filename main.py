def dec(list):
    print(sorted(list))


def ced(list):
    print(sorted(list, reverse=True))


def edc(f, list):
    f(list)


edc(dec, [1, 4, 5, 6, 78, 32, 234, ])

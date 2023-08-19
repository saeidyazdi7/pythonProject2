def lens(*args):
    m = args[0]
    for i in args:
        if i < m:
            m = i
    return m


print(lens(2, 4, 6))

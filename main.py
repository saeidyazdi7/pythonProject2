def my_gen(r=10):
    for i in range(r):
        yield i ** 2


g = my_gen()
print(list(g))
g2 = my_gen()
print(list(g2))

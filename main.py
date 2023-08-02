def gen():
    for i in range(1000):
        yield i ** 2


g = gen()
for i in g:
    print(i)

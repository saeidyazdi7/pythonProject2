def my_gen():
    for i in range(1000):
        yield i ** 2


g = my_gen()
for i in g:
    print(i)

def gen():
    yield 3


g = gen()
for i in g:
    if i == 4:
        g.throw(ValueError("error"))
print(i)

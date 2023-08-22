from functools import wraps


def coo(func):
    @wraps(func)
    def start(*args, **kwargs):
        gn = func()
        next(gn)
        return gn

    return start


@coo
def my_gen():
    # print("start")
    for i in range(2):
        name = yield i
        print("my name", name)


g = my_gen()
g.send("saeid")

from time import perf_counter
from functools import wraps


def time_calc(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("the runtime of", func.__name__, "is :", run_time)
        return value

    return wrapper_decorator


@time_calc
def A(y):
    s = 0
    for i in range(y):
        s += i ** 2


@time_calc
def B(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i


A(10000000)
B(10000000)

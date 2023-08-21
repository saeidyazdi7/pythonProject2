from functools import wraps
from time import perf_counter


def time_calculate(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("runtime:", func.__name__, "is", run_time)
        return value

    return wrapper_decorator


@time_calculate
def A(y):
    s = 0
    for i in range(y):
        s += i ** 2


@time_calculate
def B(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= 1


A(1000)
B(100)

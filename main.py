from functools import wraps


def memoize(func):
    memory = {}

    @wraps(func)
    def wrapper_decorator(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]

    return wrapper_decorator


@memoize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(300))

def my_gen(start, end, step=1):

    while start < end:
        yield start
        start += step


gr = my_gen(10, 20, 2)
print(list(gr))

def my_gen(even_or_add="e"):
    c = 0
    if even_or_add == "o":
        c = 1
    while True:
        yield c
        c += 2


eo = my_gen("m")
for _ in range(10):
    print(next(eo))

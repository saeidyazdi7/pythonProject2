def sumgen(lst):
    s = 0
    for i in lst:
        s += i
        yield s


sg = sumgen([1, 3, 5, 7, 9])
for i in sg:
    print(i)

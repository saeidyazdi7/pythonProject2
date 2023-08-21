def my_enumrate(sequence, start=0):
    c = start
    for i in sequence:
        yield c, i
        c += 1


list1 = ["saeid", "reza", "roham"]
for i, j in my_enumrate(list1):
    print(i, j)

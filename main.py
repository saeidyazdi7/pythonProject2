from functools import reduce

li = [1, 3, 5, 7, 9]
new = reduce(lambda x, y: x + y, li)
print(new)

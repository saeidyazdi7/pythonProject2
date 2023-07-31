number = [2, 3, 4, 5, 6, 7, 8, 9]
new = list(filter(lambda y: y % 2 == 0, number))
new2 = list(filter(lambda y: y % 2 != 0, number))
print(new)
print(new2)

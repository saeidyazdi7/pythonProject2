import copy


def func(a):
    a[0][1] = 4
    print(a)


a = [[1, 2], 3, 5]
func(copy.deepcopy(a))
print(a)

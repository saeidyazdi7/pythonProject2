def mysort(s):
    def A(x):
        print(sorted(x, reverse=True))
    def error(z):
        print("Error", z)
    def B(y):
        print(sorted(y))
    if s == "a":
        return A
    elif s == "d":
        return B
    else:
        return error


action = input(":")

func = mysort(action)

func([5, 7, 8, 9, 10, 2, 3, 1])

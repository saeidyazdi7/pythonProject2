def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def sumFact(n):
    sf = 0
    for i in range(1, n + 1):
        sf += fact(i)
    return sf


number = int(input("Enter :"))
print("sum :", sumFact(number))

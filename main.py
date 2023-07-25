def off_show(a, b):
    s = int(a - a * b / 100)
    return s


x = int(input("Enter:"))
y = int(input("Enter:"))
print(off_show(x, y))

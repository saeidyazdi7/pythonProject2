x = int(input("x:"))
y = int(input("y:"))
m = min(x, y)

for i in range(m, 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)
        break

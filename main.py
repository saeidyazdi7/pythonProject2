m = float("inf")
while True:
    n = float(input("n:"))
    if n < m:
        m = n
    s = input("Do yo continue?")
    if s.lower() == "no":
        break
print(m, "is small")
n = int(input("Enter:"))
i = 1
c = 0
while i < n:
    if n % i == 0:
        c += i
    i += 1
if c == n:
    print("Yes")

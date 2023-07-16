n = int(input("n:"))
i = 2
if n > 1:
    while i < (n // 2) + 1:
        if n % i == 0:
            print("is not")
            break
        i += 1
    else:
        print(n, "is a prime")
else:
    print(n, "is not a prime number")

def square(j):

    for i in range(1, j):
        if i ** 2 == j:
            print(f"Yes! {i}*{i}={j}")
            break
    else:
        print("NO")


x = int(input("Enter:"))
square(x)

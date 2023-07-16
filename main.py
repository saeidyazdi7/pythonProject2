x = int(input("Enter x:"))
y = int(input("Enter y:"))
z = int(input("Enter z:"))
if x < y + z and y < x + z and z < x + y:
    print("میتواند مثلث باشد")
    if x == y and y == z:
        print("متساوی الاضلاع")
    if x == y or y == z or x == z:
        print("متساوی الساقین")
    if x != y and y != z and x != z:
        print("مختلف الاضلاع")
    if x ^ 2 == y ^ 2 + z ^ 2 or y ^ 2 == x ^ 2 + z ^ 2 or z ^ 2 == y ^ 2 + x ^ 2:
        print("قائم الزاویه")
else:
    print("نمیتواند مثلث باشد")

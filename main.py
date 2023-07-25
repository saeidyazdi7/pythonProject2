def square(n):
    if n < 0:
        return False
    root = n ** 0.5
    if root == int(root):
        return True
    else:
        return False


print(square(81))
print(square(25))
print(square(-9))
print(square(24))
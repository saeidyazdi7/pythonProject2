def repeat(num, dig):
    return str(num).count(str(dig))


number = int(input("X:"))
digit = int(input("Y:"))
print(digit, "repeat", repeat(number, digit), "times")

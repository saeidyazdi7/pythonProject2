def repeat(number, digit):
    return str(number).count(str(digit))


number = int(input("Number:"))
digit = int(input("Digit:"))
print(digit, "repeat", repeat(number, digit), "times")

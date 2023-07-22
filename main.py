def repeat(number, digit):
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count


number = int(input("Number:"))
digit = int(input("Digit:"))
print(digit, "repeat", repeat(number, digit), "times")

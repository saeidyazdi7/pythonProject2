def repeat(num, dig):
    count = 0
    while num > 0:
        if num % 10 == dig:
            count += 1
        num //= 10
    return count


number = int(input("X:"))
digit = int(input("Y:"))
print(digit, "repeat", repeat(number, digit), "times")

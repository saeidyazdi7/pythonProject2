def power(n):
    if len(n) <= 1:
        return n
    else:
        return n[-1] + power(n[:-1])


e = "Saeid سلام"
print(power(e))

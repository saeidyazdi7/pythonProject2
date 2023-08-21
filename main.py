def revgen(s):
    t = len(s)
    for i in range(t - 1, -1, -1):
        yield s[i]


sg = revgen("saeid yazdi")
for ch in sg:
    print(ch, end="")

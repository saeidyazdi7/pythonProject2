def co(words):
    print("start")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "x" * len(word)


g = co(["tof", "gav", "hosh"])
next(g)
print(g.send("reza"))
print(g.send("hosh"))
print(g.send("gav"))

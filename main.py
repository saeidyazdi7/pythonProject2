def sending():
    print("ready")
    while True:
        name = yield
        print("my name:", name)


o = sending()
next(o)
o.send("saeid")
o.send("reza")
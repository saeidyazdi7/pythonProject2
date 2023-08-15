def a():
    x=10
    y=4
    print(locals())
def b():
    x=0
    y=7
    print(locals())
b()
a()
print(locals())
from time import sleep


def reverse(n):
    if n <= 0:
     return
    sleep(0.5)
    print(n)
    n -= 1
    reverse(n)


reverse(20)

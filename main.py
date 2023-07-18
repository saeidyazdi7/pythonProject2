from random import choice

coin = ["shir", "khat"]
shir = 0
khat = 0
for _ in range(1000):
    r = choice(coin)
    if r == "shir":
        shir += 1
    else:
        khat += 1
print(shir, "shir")
print(khat, "khat")

from random import choice

x = ["a", "b", "c"]
y = x.copy()
while True:
    computer = choice(y)
    answer = input(f"your guess  {computer} ? (y/n) :")
    if "y" in answer.lower():
        print("Computer Win!")
        break
    y.remove(computer)

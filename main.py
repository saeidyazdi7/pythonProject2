import time
from os import system

while True:
    choice = input("start?(y/n)")
    if "y" in choice.lower():
        hour = int(input("Enter:"))
        minute = int(input("Enter:"))
        second = int(input("Enter:"))
        total = hour * 3600 + minute * 60 + second
        print("timer strats now...")
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            system("cls")
        print("end")
    elif 'n' in choice.lower():
        print("Bye")
        break
    else:
        print("wrong!")

import random, string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
letter = string.ascii_letters
symbols = "!@#$%^&*()_+|{}:"
numbers = "123456789"
all = letter + lower + numbers + symbols
while True:
    print("Choose:\n\t1)create\n\t2)exit")
    choice = input("Enter:")
    if choice == "1":
        length = int(input("Enter your length:"))
        password = "".join((random.sample(all, length)))
        print(password)
    elif choice == "2":
        break
    else:
        print("wrong!")

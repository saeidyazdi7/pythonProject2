def char_type(c):
    if c.isdigit():
        print("Number")
    elif c.islower():
        print("Lower")
    elif c.isupper():
        print("Upper")
    else:
        print("Symbole")


x = input("Enter:")
char_type(x)

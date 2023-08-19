def show_type(ch):
    if "0" <= ch <= "9":
        print("Number")
    elif "a" <= ch <= "z":
        print("Upper")
    elif "A" <= ch <= "Z":
        print("Lower")
    else:
        print("Other")


c = input("Enter:")
show_type(c)

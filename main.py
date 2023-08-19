def show_type(ch):
    if 48 <= ord(ch) <= 57:
        print("Number")
    elif 65 <= ord(ch) <= 90:
        print("Upper")
    elif 97 <= ord(ch) <= 122:
        print("Lower")
    else:
        print("Other")


c = input("Enter:")
show_type(c)

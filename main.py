while True:
    print("select you option:\n\tEncrypt\n\tDecrypt\n\tExit")
    choice = input("Your choice:")
    if choice == "Encrypt":
        plain_text = input("Text:")
        encrypted_text = ""
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print("encrypted_text :", encrypted_text)
        print("*" * 40)

    elif choice == "Decrypt":
        encrypted_text = input("Text:")
        plain_text = ""
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print("plain_text :", plain_text)
        print("*" * 40)
    elif choice == "Exit":
        print("Bye")
        break
    else:
        print("wrong!")

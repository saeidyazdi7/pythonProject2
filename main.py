from functools import wraps

users = {"saeid": "13579", "reza": "24680"}
blacklist = {"saeid"}


def ban(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in blacklist:
            print("You are black")
        else:
            func(*args, **kwargs)

    return inner


@ban
def print_password(username):
    print(username, ":", users[username])


@ban
def change_password(username, new_password):
    users[username] = new_password
    print(username, ":", users[username])


print_password("saeid")
change_password("reza", "2244668800")
print(users)

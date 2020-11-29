def CheckPass(Min):
    Password = input("Your password is :")
    while len(Password) < Min:
        print("Password is Unavailable")
        Password = input("The password must be {0} or more than {0} characters".format(Min))
    return Password


def main():
    Min = 8
    AvailablePass = CheckPass(Min)
    print(len(AvailablePass) * '*')


if __name__ == '__main__':
    main()

def main():
    email_name = {}
    user_input = input("Email: ")
    while user_input != "":
        name = get_name(user_input)
        check = input("Is your name {}? (Y/n) ".format(name))
        if check.upper() != "Y" and check != "":
            name = input("Name: ")
        email_name[user_input] = name
        user_input = input("Email: ")

    for user_input, name in email_name.items():
        print("{} ({})".format(name, user_input))


def get_name(user_input):  # get name form like "Linda Ward"
    split_1 = user_input.split('@')[0]
    split_2 = split_1.split('.')
    name = " ".join(split_2).title()
    return name


main()

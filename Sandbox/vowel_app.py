def main():
    # ask the user for input
    your_name = input("Enter your name: ")

    # check how many vowels the name has
    vowels = 0
    for char in your_name:
        if char.lower() in "aeiou":
            vowels += 1

    # print the output
    print("Out of {} letters, {} has {} vowels".format(len(your_name), your_name, vowels))


if __name__ == '__main__':
    main()

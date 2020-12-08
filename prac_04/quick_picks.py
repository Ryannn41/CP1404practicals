import random

number_per_line = 6
min = 1
max = 45


def main():
    qp_numbers = int(input("How many quick picks? "))
    while qp_numbers < 0:
        print("Invalid number, please try again.")
        qp_numbers = int(input("How many quick picks? "))

    for i in range(qp_numbers):
        quick_pick = []
        for j in range(number_per_line):
            number = random.randint(min, max)
            while number in quick_pick:
                numebr = random.randint(min, max)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{}".format(number) for number in quick_pick))


main()

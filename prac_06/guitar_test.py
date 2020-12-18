from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 200000

    guitar1 = Guitar(name, year, cost)
    guitar2 = Guitar("Another Guitar", 2013, 5000)

    print("{} get_age() - Expected {}. Got {}".format(guitar1.name, 98, guitar1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar2.name, 7, guitar2.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name, True, guitar1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar2.name, False, guitar2.is_vintage()))


main()

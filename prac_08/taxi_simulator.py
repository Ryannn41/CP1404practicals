from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

Menu = "Let's drive!\nq)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(Menu)
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            print("Taxis available: ")
            show_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            taxi_chosen = taxis[taxi_choice]

        elif user_input == "d":
            taxi_chosen.start_fare()
            distance_drive = float(input("Drive how far? "))
            taxi_chosen.drive(distance_drive)
            cost = taxi_chosen.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi_chosen.name, cost))
            total_bill += cost

        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(Menu)
        user_input = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: ")
    show_taxis(taxis)


def show_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    # drive bus (input/loop is oblivious to fuel)
    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()

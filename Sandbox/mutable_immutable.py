def add_one(some_list):
    for i in range(len(some_list)):
        some_list[i] += 1


def add_two(a_number):
    a_number += 2


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
add_one(my_list)  # passing in a mutable list or by reference
print(my_list)

my_number = 18
add_two(my_number)  # passing in by value or immutables
print(my_number)

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# line1: random number between 5 and 20, smallest number is 5, largest number is 20.
# line2: even number between 3 and 10, smallest number is 3, largest number is 9.
# line2 can not produce a 4.
# line3: a random floating number between 2.5 and 5.5,
# smallest number is 2.5605914422427043, largest number is 5.435995825487218.

print(random.randint(1, 100))
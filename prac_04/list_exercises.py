numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Number: {}".format(numbers[0]))
print("Number: {}".format(numbers[1]))
print("Number: {}".format(numbers[2]))
print("Number: {}".format(numbers[3]))
print("Number: {}".format(numbers[4]))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the number is {}".format(sum(numbers) / len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Enter your username: ")
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")


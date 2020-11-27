outfile = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=outfile)
outfile.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
print(num1 + num2)
in_file.close()

in_file = open("numbers.txt", "r")
sum = 0
for num in in_file:
    sum += int(num)
print(sum)
in_file.close()
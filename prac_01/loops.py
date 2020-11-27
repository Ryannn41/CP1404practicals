for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num = int(input('Enter a number: '))
print('Number of stars:', num)
for i in range(0, num):
    print('*', end='')
print()
for i in range(0, num):
    for j in range(0, i + 1):
        print('*', end='')
    print()

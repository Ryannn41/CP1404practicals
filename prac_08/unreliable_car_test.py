from prac_08.unreliable_car import UnreliableCar

reliable_car = UnreliableCar('Reliable', 100, 90)
unreliable_car = UnreliableCar('Unreliable', 100, 20)

for i in range(1, 10):
    print('Drove {}km'.format(i))
    print('{} drove {}km'.format(reliable_car.name, reliable_car.drive(i)))
    print('{} drove {}km'.format(unreliable_car.name, unreliable_car.drive(i)))

print(reliable_car)
print(unreliable_car)

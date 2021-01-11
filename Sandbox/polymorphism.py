class Animal(object):
    def eat(self):
        print('animal eat...')


class Dog(Animal):
    def eat(self):
        print('Dog eat bones')


class Cat(Animal):
    def eat(self):
        print('Cat eat fish')


class Person:
    def eat(self):
        print('Person eat rice')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
print('----------------------------------------------')
fun(Person())

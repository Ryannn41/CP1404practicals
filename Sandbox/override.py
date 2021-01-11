class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('Name: {}\nage: {}'.format(self.name, self.age))


# def derived class
class Student(Person):
    def __init__(self, name, age, stu_num):
        super().__init__(name, age)
        self.stu_num = stu_num

    def info(self):
        super().info()
        print('Student number: {}'.format(self.stu_num))


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super().info()
        print('Year of teaching: {}'.format(self.teachofyear))


stu = Student('Ryan', 25, '4141')
teacher = Teacher('Sensei', 34, 10)

stu.info()
print('-----------------------------------------')
teacher.info()

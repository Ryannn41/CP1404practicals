class Student:
    native_place = 'JCU'  # class property

    # initial method
    def __init__(self, name, age):
        self.name = name  # self.name 实体属性，进行了一个赋值的操作，讲局部变量name的值献给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('Students are eating...')

    # staticmethod
    @staticmethod
    def method():
        print('I use staticmethod...')

    # classmethod
    @classmethod
    def cm(cls):
        print('I use classmethod...')


# class property usage
# class property shared by all method in class
# print(Student.native_place)
stu1 = Student('Alice', 20)
stu2 = Student('Sam', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = 'Shanghai'
print(stu1.native_place)
print(stu2.native_place)

print('----------------- classmethod usage ---------------------')
Student.cm()

print('----------------- staticmethod usage ---------------------')
Student.method()



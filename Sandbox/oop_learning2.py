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


# def outside class called function, inside class called method

# function
def drink()
    print('Students are drinking...')

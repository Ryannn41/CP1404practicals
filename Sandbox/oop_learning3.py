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
def drink():
    print('Students are drinking...')


"""创建Student类的对象"""

stu1 = Student('Alice', 20)
print(id(stu1))  # 1883832929248
print(type(stu1))  # <class '__main__.Student'>
print(stu1)  # <__main__.Student object at 0x000001B69D314BE0>
print('----------------------------------')
print(id(Student))
print(type(Student))
print(Student)
print('----------------------------------')
stu1.eat()  # 调用 invoke
print(stu1.name)
print(stu1.age)
print('-----------------------------------')
Student.eat(stu1)  # 调用 invoke，功能同上，invoke eat method in Student

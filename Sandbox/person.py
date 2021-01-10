
class Person:

    def __init__(self, name="", age=""):
        self.name = name
        self.age = age

    def __str__(self):
        return "Your name is {} and you are {} years old.".format(self.name, self.age)


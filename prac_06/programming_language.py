class ProgrammingLanguage:

    def __init__(self):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.type, self.reflection, self.year)

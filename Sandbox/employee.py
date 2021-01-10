from person import Person


class Employee(Person):

    def __init__(self, name="", age="", salary=0):
        super().__init__(name, age)  # Person.__init__(self, name, age)
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary = (percentage/100 + 1) * self.salary

    def __str__(self):
        return Person.__str__(self) + "\nSalary: {}".format(self.salary)

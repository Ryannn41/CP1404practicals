from employee import Employee

def main():
    my_employee = Employee("Flash Gordon", "25", 4000)
    print(my_employee)
    print("After 5% increase in salary")
    my_employee.increase_salary(5)
    print(my_employee)


if __name__ == '__main__':
    main()
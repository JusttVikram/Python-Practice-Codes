class Student:
    def __init__(self, name, physics, chemistry, Maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.Maths = Maths

    def marks_average(self):
        average_marks = (self.physics + self.chemistry + self.Maths) / 3
        print('average of marks : ', average_marks)


class Account:
    def __init__(self, acc, balance):
        self.account_no = acc
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print('Rs.', amount, ' was credited into account number ', self.account_no)

    def debit(self, amount):
        self.balance -= amount
        print('Rs.', amount, ' was debited from account number ', self.account_no)

    def check_balance(self):
        print('Your account balance is : ', self.balance)


<<<<<<< HEAD
class Circle:
    def __init__(self, radius):
        self.radius = radius
        print('Circle Created.')

    def calculate_area(self):
        area = (3.14 * self.radius ** 2)
        print(f'Area of the circle is : {area}')

    def calculate_perimeter(self):
        perimeter = (2 * 3.14 * self.radius)
        print(f'Perimeter of the circle is : {perimeter}')


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f'Role of the Employee is : {self.role}.')
        print(f'Department of the Employee is : {self.department}.')
        print(f'Salary of the Employee is : Rs.{self.salary}.')


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'IT', '80,000')


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

=======
>>>>>>> 42dba1c1bc2fb92fda997ea9edc67b8ddaa29432

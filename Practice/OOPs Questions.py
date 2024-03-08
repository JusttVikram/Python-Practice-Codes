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


class Car:
    color = 'Zed Black'

    @staticmethod
    def start():
        print('Vroom Vroom... Car Started.')

    @staticmethod
    def stop():
        print('Hussshhhhh... Car Stopped.')


class BMWCar(Car):
    def __init__(self, name):
        self.name = name
        print('Car Created.')


class A:
    varA = 'Welcome to class A'


class B:
    varB = 'Welcome to class B'


class C(A, B):
    varC = 'Welcome to class C'


obj1 = C()
print(obj1.varA)
print(obj1.varB)
print(obj1.varC)



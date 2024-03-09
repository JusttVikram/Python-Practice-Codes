class Student:
    def __init__(self, name, physics, chemistry, Maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.Maths = Maths

    def marks_average(self):
        average_marks = (self.physics + self.chemistry + self.Maths) / 3
        print('average of marks : ', average_marks)

    # def calculate_percentage(self):
    #     return str((self.physics + self.chemistry + self.Maths) / 3) + '%'

    @property
    def calculate_percentage(self):
        return str((self.physics + self.chemistry + self.Maths) / 3) + '%'


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


class Person:
    name = 'Anonymous'

    # def change_name(self, name):
    #     self.__class__.name = name
    #     # Person.name = name
    #     print(f'Updated name is {name}.')

    @classmethod
    def change_name(cls, name):
        cls.name = name


# Dunder Function
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(f'{self.real}i + {self.img}j')

    def __add__(self, num2):
        NewReal = self.real + num2.real
        NewImg = self.img + num2.img
        return Complex(NewReal, NewImg)

    def __sub__(self, num2):
        NewReal = self.real - num2.real
        NewImg = self.img - num2.img
        return Complex(NewReal, NewImg)


num1 = Complex(2, 3)
num1.show_number()

num2 = Complex(4, 6)
num2.show_number()

(num2 - num1).show_number()



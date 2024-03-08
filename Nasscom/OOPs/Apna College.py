class Student:
    college_name = "ACE"

    def __init__(self, fullname, age):
        self.name = fullname
        self.age = age
        print("Adding new student to the database...")

    def welcome(self):
        print('Welcome', self.name)

    def get_age(self):
        print('Your age : ', self.age)


s1 = Student("Karan", 18)
print(s1.name)
print(s1.age)
s1.welcome()
s1.get_age()

s2 = Student("Arjun", 20)
print(s2.name)
print(s2.college_name)
s2.welcome()
s2.get_age()




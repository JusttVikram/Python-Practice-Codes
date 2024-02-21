class A:
    """Coding maze maze main..."""
    
    age = input("Enter your age : ")
    name = input("Enter your name : ")

obj = A()
print(obj.age)
print(obj.name)
print(obj.__doc__)


class B:
    def walks(name, age):
        print(f"{name} walks in the age of {age}")

age = input("Enter your age : ")
name = input("Enter your name : ")
B.walks(name, age)


class C:
    def Details(age, name, address):
        print(age, name, address, sep=" ")

age = input("Enter your age : ")
name = input("Enter your name : ")
address = input("Enter your address : ")


C.Details(age,name, address)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} meows.")

class A:
    def __init__(self):
        self.num1 = int(input("Enter the number 1 : "))
        self.num2 = int(input("Enter the number 2 : "))

    def Add(self):
        return self.num1 + self.num2
    def Subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1* self.num2
    def division(self):
        return self.num1/ self.num2
    def remainder(self):
        return self.num1 % self.num2
    

class B:
    back = "Oracle Database and java"
    def backend(self):
        print("Back task implementation ", self.back)

class C:
    front = "HTML, CSS, JS"
    def frontend(self):
        print("Frontend task implementation", self.front)

class D (B,C):
    def show(self):
        print("Dynamic web created.")

object = D()
object.backend()
object.frontend()
object.show()

# Creating instances of the classes
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# # Calling the speak method
# animal.speak()
# dog.speak()
# cat.speak()
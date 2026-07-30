class Student:
    def __init__(self, name, age,email,phone):
        self.name = name
        self.age = age
        self.email=email
        self.phone=phone

class Principal:
    def __init__(self, name, age,email,phone):
        self.name = name
        self.age = age
        self.email=email
        self.phone=phone


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
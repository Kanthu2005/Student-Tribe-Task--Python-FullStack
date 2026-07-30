class Student:
    def __init__(self, name, age, roll_no, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, Marks: {self.marks}")
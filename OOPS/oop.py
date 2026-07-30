class Student:
    def __init__(self,name,age,roll_no,marks):
        self.name=name
        self.age=age
        self.roll_no=roll_no
        self.marks=marks
    def print_details(self):
        print(f"name:{self.name}, age:{self.age}, roll_no:{self.roll_no}, marks:{self.marks}")
s1=Student("Kanthu",20,101,85)
s2=Student("Ravi",21,102,90)
s2.print_details()
s1.print_details()    
            
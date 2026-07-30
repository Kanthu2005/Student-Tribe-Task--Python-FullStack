#single inheritance
'''class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

laborador = Dog()
laborador.eat()  # Inherited method from Animal class
laborador.bark()  # Method from Dog class
'''


#multiple inheritance
'''''
class Animal:
    def eat(self):
        print("Animal is eating.")
        
class Bird:
    def fly(self):
        print("Bird is flying.")

class Eagle(Animal, Bird):
    def hunt(self):
        print("Eagle is hunting.")

eagle = Eagle()
eagle.eat()  # Inherited method from Animal class
eagle.fly()  # Inherited method from Bird class
eagle.hunt()  # Method from Eagle class
'''
#multilevel inheritance
'''
class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping.")

puppy = Puppy()
puppy.eat()  # Inherited method from Animal class
puppy.bark()  # Inherited method from Dog class
puppy.weep()  # Method from Puppy class

'''
#hierarchical inheritance
'''
class Animal:
    def eat(self):
        print("Animal is eating.")
            
class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing.")

dog = Dog()
cat = Cat()

dog.eat()  # Inherited method from Animal class
dog.bark()# Method from Dog class


cat.eat()  # Inherited method from Animal class
cat.meow()  # Method from Cat class
'''
#hybrid inheritance
class Animal:
    def eat(self):
        print("Animal is eating.")
class Dog(Animal):
    def bark(self):
        print("Dog is barking.")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing.")
class Kitten(Cat,Animal,Dog):
    def purr(self):
        print("Kitten is purring.")    
kitten = Kitten()
kitten.eat() # Inherited method from Animal class
kitten.meow() # Inherited method from Cat class
kitten.purr() # Method from Kitten class

class Cat:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def info(self):
        print(f"I am cat, My name is {self.name} and I am {self.age} years old.")


    def make_sound(self):
        print("Meow!")


class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def info(self):
        print(f"I am Dog, My name is {self.name} and I am {self.age} years old.")


    def make_sound(self):
        print("Woof Woof!")

cat1 = Cat("Tom", 3)
dog1 = Dog("Ben", 6)

for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can walk and run")



class Lion(Animal):
    def move(self):
        print("I can walk, run and hunt")


Human = Human()
Human.move()


Snake = Snake()
Snake.move()

Dog = Dog()
Dog.move()

Lion = Lion()
Lion.move()
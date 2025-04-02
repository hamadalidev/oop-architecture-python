from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory Method
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Usage
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Output: Woof!

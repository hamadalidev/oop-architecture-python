class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Car(Engine, Wheels):
    pass

my_car = Car()
print(my_car.start())  # Output: Engine started
print(my_car.rotate())  # Output: Wheels rotating

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Calls parent class constructor
        self.model = model

    def show_model(self):
        return f"Model: {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.show_brand())  # Output: Brand: Toyota
print(car1.show_model())  # Output: Model: Corolla

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Car: {self.brand} {self.model}"

# Creating objects
car1 = Car("Tesla", "Model S")
print(car1.display_info())  # Output: Car: Tesla Model S

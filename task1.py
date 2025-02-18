class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")

# Create two car objects
car1 = Car("Honda", "xrm", 2020)
car2 = Car("rusi", "chariot", 2021)

# Display their details
car1.display_info()
car2.display_info()
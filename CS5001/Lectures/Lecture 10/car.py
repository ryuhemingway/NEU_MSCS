import numpy as np

class Car:
    def __init__(self, make, model, year, price, new_features):
        self.make           = make
        self.model          = model
        self.year           = year
        self.price          = price
        self.new_features   = new_features
        self.feature_prices = {"leather_seats": 5000, "speaker": 1000,
                               "air_suspension": 10000, "new_color": 2000}

    def __str__(self):
        return "This car is a {} {} manufactured in {} costing {}.".format(
            self.make, self.model, self.year, self.price)

    def update_price(self):
        self.price += np.dot(self.new_features,
                             np.array(list(self.feature_prices.values())))

my_car = Car("Toyota", "Fortuner", 2025, 50000, [1, 0, 0, 1])

my_car.update_price()
print(f"Make: {my_car.make}") 
print(f"New Price: {my_car.price}") 
print(f"new_"
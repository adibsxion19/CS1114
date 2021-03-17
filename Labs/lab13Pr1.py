#Aadiba Haque
#Lab 13 Problem 2
#May 1 2020
class Odometer:
    def __init__(self):
        self.mileage = 0
    def __str__(self):
        return "mileage: {}".format(self.mileage)
    def __repr__(self):
        return "mileage: {}".format(self.mileage)
    def get_mileage(self):
        return self.mileage
    def add_mileage(self, miles):
        self.mileage += miles
    def reset_mileage(self):
        self.mileage = 0

        
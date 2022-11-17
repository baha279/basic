
class Car:

    # attribute - required, optional ( default)
    # behaviour - GRUD --> SET,GET, OTHER
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = 0

    def get_description(self):
          print(f"Car details: \nManufacturer: {self.make}'\nModel:{self.model}\nYear{self.year}")
          print(f"Current Mileage: {self.mileage}")
    def set_mileage(self, new_mileage):
        if new_mileage > self.mileage
            self.mileage = new_mileage
            

car1 = Car('bmw', 'x5', '2022')
print(car1.make, car1.year+1)
car1.get_description()
print('## Setters - updating the values of attributes')
car1.mileage = 50
car1.get_description()
car1.mileage = 10
car1.get_description()




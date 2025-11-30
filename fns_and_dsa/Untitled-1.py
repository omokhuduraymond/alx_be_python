class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        name = f"{self.year} {self.make} {self.model}"
        return name

    def odometer_reading(self):
        print(f"This car has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increase_odometer(self, miles):
        self.odometer += miles


mycar = Car("Toyota", "Camry", 2020)
print(mycar.get_descriptive_name())

mycar.odometer_reading()
mycar.update_odometer(100)
mycar.odometer_reading()
mycar.increase_odometer(50)
mycar.odometer_reading()
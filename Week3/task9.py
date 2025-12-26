# Vehicle → Car (Method Overriding) 
# ● Create a base class Vehicle with brand and year. 
# ● Create a child class Car that adds model. 
# ● Override a method info() in Car. 
# ● Test info() for both classes. 
class Vihecle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")    
class Car(Vihecle):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Model: {self.model}")


vehicle=Vihecle("Toyota",2020)
vehicle.info()
car=Car("Honda",2021,"Civic")
car.info()
# 3. Car Class 
# ● Create a class Car with attribute make. 
# ● Add a method get_make() that returns the make. 
# ● Test it with an object.
class Car:
    def __init__(self,make):
        self.make = make
    def get_make(self):
        return self.make
car = Car('nisan')       
print(car.get_make()) 

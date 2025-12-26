# Animal & Cat Classes (Inheritance) 
# ● Create a base class Animal and a child class Cat. 
# ● Add a make_sound() method for each. 
# ● Test by calling the method on both objects. 
class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
animal = Animal()
animal.make_sound()
cat=Cat()
cat.make_sound()            
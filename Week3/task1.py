# 1. Person Class 
# ● Create a class Person with attributes name and age. 
# ● Make an object and print its attributes.
class Person:
    def __init__(self,name ,age):
        self.name =name
        self.age =age
person = Person("John", 30)
print(person.name)
print(person.age)
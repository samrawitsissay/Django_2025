# 4. Rectangle Class 
# ● Create a class Rectangle with width and height. 
# ● Print the area (without adding a separate method). 
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):        
        return self.length * self.width
rect = rectangle(5, 10)
print("Area of rectangle:", rect.area())   
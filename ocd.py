from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type

        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]

        if self.shape_type == "circle":
            self.redius = kwargs["redius"]


    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        
        elif self.shape_type == "circle":
            return pi * self.redius**2


rectangle = Shape("rectangle", width = 10, height = 5)
area = rectangle.calculate_area()
print(area)


circle = Shape("circle", redius = 7)
area1 = circle.calculate_area()
print(area1)
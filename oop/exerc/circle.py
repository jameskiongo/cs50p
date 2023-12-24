class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return f"{self.radius}"
    def calculate_area(self):
        n = 3.142
        return (n * (self.radius * self.radius))
    def perimeter(self):
        n = 3.142
        return (2 * n * self.radius)

circle = Circle(14)

area = circle.calculate_area()
perimeter = circle.perimeter()

print(area, perimeter)

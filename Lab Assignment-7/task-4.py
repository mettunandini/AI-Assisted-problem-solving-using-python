class Rectangle:
    def __init__(self, length, width):  
        # ✅ include 'self' as the first parameter
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Example usage
rect = Rectangle(10, 5)
print("Length:", rect.length)
print("Width:", rect.width)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

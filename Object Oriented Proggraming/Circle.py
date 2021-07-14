import math


class Circle:
    """
    Окружность (Circle)
    Площадь (area) = Pi * R**2
    perimeter = 2 * Pi * R
    """
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        """Площадь"""
        return math.pi * self.radius

    def get_length(self) -> float:
        """Длина (периметр)"""
        return (2 * math.pi * self.radius)

    def get_diameter(self) -> int:
        """Диаметр"""
        return 2 * self.radius

# first_circle = Circle()
# second_circle = Circle(radius=30)

# print(first_circle.get_area())
# print(second_circle.get_diameter())
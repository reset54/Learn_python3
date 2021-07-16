class Point():
    """Класс для предоставления точек в пространстве"""
    x = 1
    y = 1
    def __init__(self, x=0, y=0, list=[]):
      print("\nБыл создан экземпляр класса Point")
      self.x = x
      self.y = y
      self.list = list
      list.append(self)
      print(self.__str__(),)
      print(list)
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print(self.__dict__)



print(f"Документация = {Point.__doc__}")
print(f"Имя класса =   {Point.__name__}")

pt = Point() # создаём экземляр класса pt
pt.x = 100
print(f"\npt.x = {pt.x}\npt.y = {pt.y}")

print(pt.__dict__) # y не переопределён
setattr(pt, "z", 7)
pt.set_coords(4, 10)
pt1 = Point()
pt1.set_coords(2, 8)
pt2 = Point()
pt2.set_coords(1, 4)
pt3 = Point()
pt3.set_coords(45, 10)


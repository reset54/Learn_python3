import sys

if len(sys.argv) < 2:
    print("Пожалуйста передайте в аргумент терминала сторону квадрата!")
    exit()
square_side = sys.argv[1]
if not square_side.isnumeric():
    print("Пожалуйста передайте числовое значение в качестве аргумента длины стороны квадрата!")
    exit()
perimeter = float(square_side) * 4
# print(sys.argv)
# print(type(sys.argv))
print(f"Периметр квадрата со стороной {square_side} равен {perimeter}")

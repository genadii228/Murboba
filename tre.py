import math

x1, y1 = map(float, input("Введите координаты точки A (x y): ").split())
x2, y2 = map(float, input("Введите координаты точки B (x y): ").split())
x3, y3 = map(float, input("Введите координаты точки C (x y): ").split())

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
CA = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

perimeter = AB + BC + CA

print(f"Периметр треугольника: {perimeter}")

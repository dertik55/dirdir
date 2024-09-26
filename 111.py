from math import *

for i in range(5):
    a = float(input("Введите число a для z1: "))
    z1 = cos(a) + sin(a) + cos(3 * a) * sin(3 * a)
    print(f"Полученное значение z1 = {z1}")

    a = float(input("Введите число a для z2: "))
    z2 = 2 * sqrt(2) * cos(a) * sin((pi/4) + (2 * a))
    print(f"Полученное значение z2 = {z2}")




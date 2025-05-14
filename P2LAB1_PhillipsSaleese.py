# Saleese Phillips
# 02-20-2025
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle from a given radius.

import math

radius = input("What is the radius of the circle? ")
radius = float(radius)  # Convert input to float

diameter = radius * 2
circumference = math.pi * radius * 2
area = math.pi * radius ** 2

print("The diameter of the circle is", round(diameter, 1))
print("The circumference of the circle is", round(circumference, 2))
print("The area of the circle is", round(area, 3))
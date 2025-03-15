# Created by: Serge Hamouche
# Created on: march 15rd, 2025
# This program asks the user for the radius of the circle
# It then calculates and displays the area and perimeter of
# The circle
import math


# Input
radius = int(input("Enter the radius of the circle:"))

# Process
Area = math.pi * radius**2
diameter = 2 * radius

# Output
print(Area, diameter)

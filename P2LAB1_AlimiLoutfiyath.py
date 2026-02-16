# Loutfiyath Alimi
# 2/16/2026
# P2LAB1
# Using a library with formula of circle

import math

print(math.pi)


# Get a radious  from the user as a float
radius = float(input("What is the radius of the circle? "))

print()

# Calculate diameter
diameter = 2 * radius

# Display Diameter
print(f"The diameter of the circle is {diameter:.1f}")

print()

# calculate circumference
circumference = 2 * math.pi * radius

# Display circumference
print(f"The circumference of the circle is {circumference:.2f}")

print()

# Calculate the area
area = math.pi * math.pow(radius,2)

# Display the area

print(f"The area is {area:.3f}")